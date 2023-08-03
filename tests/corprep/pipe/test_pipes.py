from corprep.datasets.similarity import find_similar_docs_ac
from corprep.datasets.filter import filter_dataset
from corprep import HyFI
from hyfi.composer import PipeTargetTypes


def test_pipes():
    HyFI.generate_pipe_config(
        find_similar_docs_ac, pipe_target_type=PipeTargetTypes.GENERAL_EXTERNAL_FUNCS
    )
    HyFI.generate_pipe_config(
        filter_dataset,
        pipe_target_type=PipeTargetTypes.GENERAL_EXTERNAL_FUNCS,
    )


if __name__ == "__main__":
    test_pipes()
