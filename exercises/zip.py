def zip (array_one: list[str], array_two: list[int]) -> dict:
    if len(array_one) != len(array_two):
        return {}
    if len(array_one) == 0 or len(array_two) == 0:
        return {}
    
    result: dict[str, int] = {}

    for idx in range(0,len(array_one)):
        result[array_one[idx]] = array_two[idx]

    return result

print(zip([],[]))
print(zip(["a","b","c"],[1,2]))
print(zip(["a","b","c"],[1,2,3]))