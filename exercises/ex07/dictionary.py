"""This'll do something."""
__author__ = "730566506"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    return_dict: dict[str, str] = {}
    for key in given:
        for check_key in return_dict:
            if check_key == given[key]:
                raise KeyError("The same key appears twice :(")
        return_dict[given[key]] = key
    return return_dict


def favorite_color(given: dict[str, str]) -> str:
    """Find the fav color."""
    count_list: list[str] = []
    for key in given:
        count_list.append(given[key])
    output = count(count_list)
    maxim: int = 0
    return_str: str = ""
    for key in output:
        if output[key] >= maxim:
            output[key] = maxim
            return_str = key
    return return_str


def count(given: list[str]) -> dict[str, int]:
    """Counts up a glist."""
    result: dict[str, int] = {}
    for elem in given:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result


