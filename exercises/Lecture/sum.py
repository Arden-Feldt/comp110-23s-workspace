"""Example Function for unit tests."""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs"""
    sum_total: float = 0.0
    for i in range(len(xs)):
        sum_total += xs[i]
        i += 1
    return sum_total