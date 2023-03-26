"""Tests for utils, and make it a little longer."""
__author__ = "730566506"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_one_option() -> None:
    """Tests only_evens with only one even number."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_only_evens_no_evens() -> None:
    """Tests only_evens with an empty list."""
    test_list: list[int] = [1, 5, 33]
    assert only_evens(test_list) == []


def test_only_evens_only_evens() -> None:
    """Tests only_evens with only even numbers."""
    test_list: list[int] = [2, 2, 4, 4, 6, 6]
    assert only_evens(test_list) == [2]


def test_sub_whole_list() -> None:
    """Tests sub by sub-ing whole list."""
    test_list: list[int] = [1, 2, 3]
    assert sub(test_list, 0, 4) == [1, 2, 3]


def test_sub_some_list() -> None:
    """Tests sub by sub-ing some of the list."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, 1, 3) == [1, 2]


def test_sub_no_list() -> None:
    """Tests sub by sub-ing empty list."""
    test_list: list[int] = []
    assert sub(test_list, 0, 0) == []


def test_concat_empty_lists() -> None:
    """Tests concat with empty list."""
    test_list_one: list[int] = []
    test_list_two: list[int] = []
    assert concat(test_list_one, test_list_two) == []


def test_concat_two_lists() -> None:
    """Tests concat with two list."""
    test_list_one: list[int] = [1, 2, 3]
    test_list_two: list[int] = [4, 5, 6]
    assert concat(test_list_one, test_list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_same_lists() -> None:
    """Tests concat with two identical lists."""
    test_list_one: list[int] = [1]
    test_list_two: list[int] = [1]
    assert concat(test_list_one, test_list_two) == [1, 1]