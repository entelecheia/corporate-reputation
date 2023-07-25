from typing import List, Optional

from datasets import Dataset

from corprep import HyFI

logger = HyFI.getLogger(__name__)


def tokenize_dataset(
    data: Dataset,
    tokenizer_config_name: str = "simple",
    num_proc: int = 1,
    batched: bool = True,
    text_col: str = "bodyText",
    token_col: str = "tokenizedText",
    load_from_cache_file: bool = True,
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

    data = data.map(
        pos_tagging,
        num_proc=num_proc,
        batched=batched,
        load_from_cache_file=load_from_cache_file,
    )
    logger.info("POS tagging done.")
    if verbose:
        print(data[0][token_col])
    return data


def extract_tokens(
    data: Dataset,
    tokenizer_config_name: str = "simple",
    num_proc: int = 1,
    batched: bool = True,
    token_col: str = "tokenizedText",
    nouns_only: bool = False,
    postags: Optional[List[str]] = None,
    stop_postags: Optional[List[str]] = None,
    strip_pos: Optional[bool] = None,
    postag_delim: Optional[str] = None,
    postag_length: Optional[int] = None,
    load_from_cache_file: bool = True,
    verbose: bool = False,
) -> Dataset:
    def pos_tagging(batch):
        tokenizer = HyFI.instantiate_config(f"tokenizer={tokenizer_config_name}")
        batch_tokens = []
        for tokens in batch[token_col]:
            batch_tokens.append(
                tokenizer.extract(
                    tokens,
                    nouns_only=nouns_only,
                    postags=postags,
                    stop_postags=stop_postags,
                    strip_pos=strip_pos,
                    postag_delim=postag_delim,
                    postag_length=postag_length,
                )
            )
        return {token_col: batch_tokens}

    data = data.map(
        pos_tagging,
        num_proc=num_proc,
        batched=batched,
        load_from_cache_file=load_from_cache_file,
    )
    logger.info("POS tagging done.")
    if verbose:
        print(data[0][token_col])
    return data
