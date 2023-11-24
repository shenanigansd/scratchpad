from itertools import combinations


def find_distinct_sum(lst: list[int], target: int) -> bool:
    return any(sum(tup) == target for tup in combinations(lst, 2))
