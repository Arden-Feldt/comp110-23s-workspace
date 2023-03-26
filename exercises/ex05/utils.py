"""utils, but make it longer as to not get an error."""
__author__ = "730566506"


def only_evens(array: list[int]) -> list[int]:
    """Returns list of even ints."""
    result_array: list[int] = []
    for num in array:
        if num % 2 == 0:
            result_array.append(num)
    return result_array


def concat(array_one: list[int], array_two: list[int]) -> list[int]:
    """Concats two lists."""
    result_array: list[int] = array_one + array_two
    return result_array
    

def sub(array: list[int], start: int, end: int) -> list[int]:
    """Returns a shorted list from [start,end)."""
    if start < 0:
        start = 0
    if end > len(array):
        end = len(array)
    if len(array) == 0:
        return []
    if start >= len(array):
        return []
    result_array: list[int] = []
    for idx in range(start, end):
        result_array.append(array[idx])
    return result_array