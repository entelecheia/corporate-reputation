from corprep.datasets.similarity import find_similar_docs_ac
from corprep import HyFI
from hyfi.composer import PipeTargetTypes


def test_pipes():
    HyFI.generate_pipe_config(
        find_similar_docs_ac, pipe_target_type=PipeTargetTypes.GENERAL_EXTERNAL_FUNCS
    )


if __name__ == "__main__":
    test_pipes()
