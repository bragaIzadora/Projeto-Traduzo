import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history(prepare_base):
    history_json = HistoryModel.list_as_json()
    history_data = json.loads(history_json)

    expected_data = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]

    assert len(history_data) == len(expected_data)
    for expected, actual in zip(expected_data, history_data):
        assert expected["text_to_translate"] == actual["text_to_translate"]
        assert expected["translate_from"] == actual["translate_from"]
        assert expected["translate_to"] == actual["translate_to"]
