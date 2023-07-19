import random

from datasets import Dataset

from corprep import HyFI  # type: ignore

logger = HyFI.getLogger(__name__)


def sample_dataset(
    data: Dataset,
    num_samples: int = 100,
    randomize: bool = True,
    random_seed: int = 42,
    verbose: bool = False,
) -> Dataset:
    """
    Sample a dataset.
    """
    if random_seed > 0:
        random.seed(random_seed)
    if randomize:
        idx = random.sample(range(len(data)), num_samples)
    else:
        idx = range(num_samples)

    data = data.select(idx)
    logger.info("Sampling done.")
    if verbose:
        print(data)

    return data
