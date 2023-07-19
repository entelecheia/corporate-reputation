from typing import List, Optional, Union

from datasets import Dataset

from corprep import HyFI  # type: ignore
from corprep.absa.config import AbsaModel

logger = HyFI.getLogger(__name__)


def predict_each(
    text: str,
    model: AbsaModel,
):
    task = model.absa_task
    verbose = model.verbose

    response = model.predict(text)
    if verbose:
        logger.info("Task: %s | Text:\n%s\n | Response:\n%s\n", task, text, response)

    return response


def batch_predict(
    batch,
    task: str = "QUAD",
    absa_config_name: str = "default",
    text_col: str = "bodyText",
):
    cfg = HyFI.compose_as_dict(f"absa={absa_config_name}")
    model = AbsaModel(**cfg)
    model.absa_task = task
    model.init_api()
    if model.verbose:
        print(model)

    res = []
    for i, text in enumerate(batch[text_col]):
        res.append(predict_each(text, model))
    return {f"{task}_pred": res}


def predict(
    dataset: Dataset,
    tasks=["QUAD"],
    absa_config_name: str = "default",
    text_col: str = "bodyText",
    batch_size=2,
    num_workers=1,
    remove_columns: Optional[Union[List[str], str]] = None,
    load_from_cache_file=True,
    verbose=False,
) -> Dataset:
    for task in tasks:
        logger.info("Predicting %s...", task)
        dataset = dataset.map(
            batch_predict,
            batched=True,
            batch_size=batch_size,
            num_proc=num_workers,
            fn_kwargs={
                "task": task,
                "absa_config_name": absa_config_name,
                "text_col": text_col,
            },
            remove_columns=remove_columns,
            load_from_cache_file=load_from_cache_file,
        )
    if verbose:
        print(dataset[0])
    return dataset