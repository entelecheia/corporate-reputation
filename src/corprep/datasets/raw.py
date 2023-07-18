from pathlib import Path
from typing import Union

from datasets import Dataset

from corprep import HyFI  # type: ignore

logger = HyFI.getLogger(__name__)


def load_raw_dataset(
    raw_dataset_dir: Union[str, Path],
    path: str = "json",
    file_pattern: str = "*.dat",
    verbose: bool = False,
    **kwargs,
):
    raw_dataset_dir = Path(raw_dataset_dir)
    raw_data_files = []
    if raw_dataset_dir.exists():
        raw_data_files = HyFI.get_filepaths(f"{raw_dataset_dir}/{file_pattern}")
        logger.info("Found %d raw data files.", len(raw_data_files))
    else:
        logger.warning("No raw data files found.")
        raise FileNotFoundError()

    dataset = HyFI.load_dataset(path, data_files=raw_data_files)
    ds_train: Dataset = dataset["train"]  # type: ignore

    logger.info("Number of training samples: %s", len(ds_train))
    if verbose:
        print(ds_train[99])
        print(ds_train[-99])
        logger.info("Dataset features: %s", ds_train.features)

    return ds_train
