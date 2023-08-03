from typing import List, Union, Optional
import pandas as pd

from corprep import HyFI

logger = HyFI.getLogger(__name__)


def filter_dataset(
    data: pd.DataFrame,
    queries: Optional[Union[str, List[str]]] = None,
    sample_size: int = 100,
    sample_seed: int = 42,
    output_dir: str = ".",
    sample_filename: str = "sample.parquet",
    train_filename: str = "train.parquet",
    discard_filename: str = "discard.parquet",
    verbose: bool = False,
) -> pd.DataFrame:
    """
    Filter the data to remove short documents and create a sample for analysis
    """
    # Filter by queries
    if queries:
        data_ = filter_by_queries(data, queries, verbose=verbose)
    else:
        logger.warning("No query specified")
        data_ = data.copy()

    # Create a sample for analysis
    sample = data_.sample(sample_size, random_state=sample_seed)
    HyFI.save_dataframes(
        sample,
        data_file=f"{output_dir}/{sample_filename}",
        verbose=verbose,
    )

    # Create a train set
    train = data_[~data_.index.isin(sample.index)]
    HyFI.save_dataframes(
        train,
        data_file=f"{output_dir}/{train_filename}",
        verbose=verbose,
    )

    # Create a discard set
    discard = data[~data.index.isin(train.index) & ~data.index.isin(sample.index)]
    HyFI.save_dataframes(
        discard,
        data_file=f"{output_dir}/{discard_filename}",
        verbose=verbose,
    )
    logger.info(
        "Created %d samples, %d train samples, and %d discard samples",
        sample.shape[0],
        train.shape[0],
        discard.shape[0],
    )

    return train


def filter_by_queries(
    data: pd.DataFrame,
    queries: Union[str, List[str]],
    verbose=False,
) -> pd.DataFrame:
    """
    Filter the data by queries

    Args:
        data: The data to filter
        queries: The queries to filter the data by
        verbose: Whether to print verbose logs

    Returns:
        The filtered data

    Examples:
        >>> import pandas as pd
        >>> data = pd.DataFrame({"text": ["hello world", "hello", "world"]})
        >>> filter_by_queries(data, "text.str.split().str.len() >= 2")
            text
        0  hello world
        >>> filter_by_queries(data, ["text.str.contains('hello')", "text.str.contains('world')"])
            text
        0  hello world
        2        world
    """
    if isinstance(queries, str):
        queries = [queries]

    for qry in queries:
        if verbose:
            logger.info("filtering data by %s", qry)
        n_docs = data.shape[0]
        data = data.query(qry, engine="python")
        if verbose:
            logger.info("filtered %d documents", n_docs - data.shape[0])
    return data
