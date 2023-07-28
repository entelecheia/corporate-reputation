from corprep.datasets.io import load_raw_dataset
from corprep.datasets.similarity import find_similar_docs_ac
from corprep.absa.agent import absa_agent_predict
from corprep import HyFI


def test_pipes():
    HyFI.save_hyfi_pipe_config(load_raw_dataset, use_pipe_obj=False)
    HyFI.save_hyfi_pipe_config(find_similar_docs_ac)
    HyFI.save_hyfi_pipe_config(absa_agent_predict)


if __name__ == "__main__":
    test_pipes()
