"""Messing around with Lists and Functions."""
__author__ = "730566506"


def all(set_list: list[int], number: int) -> bool:
    """Looks for a number in a list."""
    idx: int = 0
    result: bool = True
    if (len(set_list) == 0):
        return False
    while (idx < len(set_list)):
        if (set_list[idx] != number):
            result = False
        idx += 1
    return result


def max(input: list[int]) -> int:
    """Finds the max int in a list."""
    idx: int = 0
    max: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while (idx < len(input)):
        if (max < input[idx]):
            max = input[idx]
        idx += 1
    return max
        

def is_equal(set_one: list[int], set_two: list[int]) -> bool:
    """Finds if two lists are deeply equivalent."""
    idx: int = 0
    result: bool = True
    if (len(set_one) != len(set_two)):
        return False
    while (idx < len(set_one)):
        if (set_one[idx] != set_two[idx]):
            result = False
        idx += 1
    return result