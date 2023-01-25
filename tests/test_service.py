from api import service


def test_filter_words():
    test_data = ["Мама", "МАМА", "Мама", "папа", "ПАПА", "ДЯдя", "брАт", "Дядя", "Дядя"]
    result = {"папа", "брат"}
    assert service.filter_words(test_data) == result


def test_filter_words_single():
    test_data = ["Python"]
    result = {"python"}
    assert service.filter_words(test_data) == result


def test_filter_words_empty():
    test_data = []
    result = set()
    assert service.filter_words(test_data) == result

