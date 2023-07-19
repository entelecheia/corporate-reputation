from datasets import Dataset
from ekonlpy.tag import Mecab  # type: ignore

from corprep import HyFI  # type: ignore

logger = HyFI.getLogger(__name__)


def tokenize_dataset(
    data: Dataset,
    num_proc: int = 1,
    batched: bool = True,
    text_col: str = "bodyText",
    verbose: bool = False,
) -> Dataset:
    def pos_tagging(batch):
        mecab = Mecab()
        batch_tags = []
        for text in batch[text_col]:
            sentences = text.split("\n")
            pos_tags = []
            for sentence in sentences:
                pos_tags.extend(mecab.pos(sentence))
            batch_tags.append(pos_tags)
        return {"pos_tags": batch_tags}

    data = data.map(pos_tagging, num_proc=num_proc, batched=batched)
    logger.info("POS tagging done.")
    if verbose:
        print(data[0]["pos_tags"])
    return data
