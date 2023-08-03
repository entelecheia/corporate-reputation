from corprep.datasets.similarity import find_similar_docs_ac
from corprep import HyFI


def test_pipes():
    HyFI.generate_config(find_similar_docs_ac, use_first_arg_as_pipe_obj=True)


if __name__ == "__main__":
    test_pipes()
