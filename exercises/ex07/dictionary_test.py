"""Tests for utils, and make it a little longer."""
__author__ = "730566506"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_base_example() -> None:
    """Teadfssts only_evens with only one even number."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_diff_example() -> None:
    """Tests adsffonly_evens with only one even number."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b'}


def test_invert_other_example() -> None:
    """Tests only_evens wiasdfsth only one even number."""
    test_dict: dict[str, str] = {'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'y': 'b', 'x': 'c'}


def test_int_base_example() -> None:
    """only_evens with ondafsdly one even nmber."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "Blue"


def test_invert_bexample() -> None:
    """Tests only_evens with only   number."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "Blue"


def test_vert_base_exle() -> None:
    """Tests   only one even number."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "Blue"


def test_iert_base_exle() -> None:
    """Tests only_evens  only one even ."""
    test_list: list[str] = ["a", "a", "b", "a"]
    assert count(test_list) == {'a': 3, 'b': 1}


def test_invert_base_exle() -> None:
    """Tests   only one even number."""
    test_list: list[str] = ["a", "a", "b", "a", "c"]
    assert count(test_list) == {'a': 3, 'b': 1, 'c': 1}


def test_invert_bse_exle() -> None:
    """Tests only_eveneven number."""
    test_list: list[str] = ["a", "b", "a", "c"]
    assert count(test_list) == {'a': 2, 'b': 1, 'c': 1}