from corprep.datasets.io import load_raw_dataset
from corprep.datasets.similarity import find_similar_docs_ac
from corprep.absa.agent import absa_agent_predict
from corprep import HyFI


def test_pipes():
    HyFI.generate_config(load_raw_dataset, use_pipe_obj=False)
    HyFI.generate_config(find_similar_docs_ac, use_first_arg_as_pipe_obj=True)
    HyFI.generate_config(absa_agent_predict, use_first_arg_as_pipe_obj=True)


if __name__ == "__main__":
    test_pipes()
