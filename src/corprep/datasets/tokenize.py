from datasets import Dataset
from ekonlpy.tag import Mecab  # type: ignore

from corprep import HyFI  # type: ignore

logger = HyFI.getLogger(__name__)


def tokenize_dataset(
    data: Dataset,
    tokenizer_config_name: str = "simple",
    num_proc: int = 1,
    batched: bool = True,
    text_col: str = "bodyText",
    token_col: str = "tokenizedText",
    verbose: bool = False,
) -> Dataset:
    def pos_tagging(batch):
        tokenizer = HyFI.instantiate_config(f"tokenizer={tokenizer_config_name}")
        batch_tokens = []
        for text in batch[text_col]:
            sentences = text.split("\n")
            tokens = []
            for sentence in sentences:
                tokens.extend(tokenizer(sentence))
            batch_tokens.append(tokens)
        return {token_col: batch_tokens}

    data = data.map(pos_tagging, num_proc=num_proc, batched=batched)
    logger.info("POS tagging done.")
    if verbose:
        print(data[0][token_col])
    return data
