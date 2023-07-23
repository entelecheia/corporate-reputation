from corprep import HyFI
from corprep.tokenizer import MecabTokenizer


def test_tokenizer():
    print(HyFI.get_caller_module_name())
    cfg = HyFI.compose_as_dict("tokenizer=mecab")
    tokenizer = MecabTokenizer(**cfg)
    # print(tokenizer)
    text = "금통위는 따라서 물가안정과 병행, 경기상황에 유의하는 금리정책을 펼쳐나가기로 했다고 밝혔다."
    tokens = tokenizer(text)
    print(tokens)
    # assert len(stop.stopwords_list) == 179


if __name__ == "__main__":
    test_tokenizer()
