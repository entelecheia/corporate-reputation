import datetime
import json
import time
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import backoff
import openai
from openai.error import (
    APIConnectionError,
    APIError,
    InvalidRequestError,
    RateLimitError,
    ServiceUnavailableError,
)
from pydantic import BaseModel

from corprep import HyFI  # type: ignore

logger = HyFI.getLogger(__name__)


class PromptConfig(BaseModel):
    tasks: Dict[str, str] = {}
    prompts: Dict[str, Dict[str, str]] = {}

    def get_prompt(self, task, prompt_name):
        if prompt := self.prompts.get(task, {}).get(prompt_name, ""):
            return prompt
        else:
            raise ValueError(f"Prompt for task {task} is not defined.")


class AbsaModel(BaseModel):
    api_key: Optional[str] = None
    model_name: str = "gpt-3.5-turbo-0301"
    rate_limit_per_minute: int = 20
    absa_task: str = "AE"
    prompts: PromptConfig = PromptConfig()
    prompt_name: str = "base"
    temperature: float = 0.0
    output_dir: str = "outputs/preds"
    save_filename: Optional[str] = None
    verbose: bool = False
    _agent_: Optional[openai.ChatCompletion] = None

    @property
    def save_filepath(self):
        model_name = self.model_name.replace(".", "")
        save_filename = (
            self.save_filename
            or f"{self.absa_task}_{self.prompt_name}_{model_name}.jsonl"
        )
        return f"{self.output_dir}/{save_filename}"

    def init_api(self, api_key: Optional[str] = None):
        api_key = api_key or self.api_key
        denv = HyFI.dotenv()
        if not api_key and denv.OPENAI_API_KEY:
            api_key = denv.OPENAI_API_KEY.get_secret_value()
        if not api_key:
            raise ValueError("OpenAI API Key is required.")
        self._agent_ = openai.ChatCompletion()
        logger.info("OpenAI ChatCompletion API is initialized.")

    def get_prompt(self, text: str):
        task = self.absa_task
        prompt = self.prompts.get_prompt(task, self.prompt_name)
        prompt += f'\nInput text:\n"{text}"\nAnswer:\n'
        return prompt

    def predict(self, text: str):
        args = {
            "model": self.model_name,
            "temperature": self.temperature,
            "messages": [
                {
                    "role": "user",
                    "content": self.get_prompt(text),
                }
            ],
        }
        delay = 60.0 / self.rate_limit_per_minute
        content, usage, _ = call_api(self._agent_, args, delay_in_seconds=delay)
        result = parse_response_to_json(content, usage, text)
        if self.save_filepath:
            append_to_jsonl(result, self.save_filepath)
        # remove text from result to save space
        del result["text"]
        return json.dumps(result, ensure_ascii=False)


def parse_response_to_json(response: str, usage: dict, text: str):
    try:
        response = json.loads(response)
        result = {
            "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
            "parsed": "success",
            "usage": usage,
            "response": response,
            "text": text,
        }
    except json.decoder.JSONDecodeError:
        result = {
            "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
            "parsed": "failed",
            "usage": usage,
            "response": response,
            "text": text,
        }
    return result


def append_to_jsonl(data, filename: str, encoding: str = "utf-8") -> None:
    """Append a json payload to the end of a jsonl file."""
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    json_string = json.dumps(data, ensure_ascii=False)
    with open(filename, "a", encoding=encoding) as f:
        f.write(json_string + "\n")


@backoff.on_exception(
    backoff.expo,
    (
        RateLimitError,
        APIConnectionError,
        APIError,
        ServiceUnavailableError,
    ),
)
def request_api(agent, args, delay_in_seconds: float = 1):
    time.sleep(delay_in_seconds)
    return agent.create(**args)


def call_api(agent, args, delay_in_seconds: float = 1) -> Tuple[str, dict, Any]:
    time.sleep(delay_in_seconds)
    try:
        response = request_api(agent, args, delay_in_seconds=delay_in_seconds)
        message = response["choices"][0]["message"]
        content = message["content"].strip().strip("\n")
        usage = response["usage"]
        return content, usage, response
    except InvalidRequestError as e:
        logger.error(e)
        usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        return str(e.user_message), usage, e
    except Exception as e:
        logger.error(e)
        usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        return str(e), usage, e
