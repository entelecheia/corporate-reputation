from corprep import HyFI
from corprep.tokenizer.stopwords import Stopwords


def test_stopwords():
    print(HyFI.get_caller_module_name())
    cfg = HyFI.compose_as_dict("stopwords")
    stop = Stopwords(**cfg)
    print(stop.stopwords_list)
    assert len(stop.stopwords_list) == 179


if __name__ == "__main__":
    test_stopwords()
