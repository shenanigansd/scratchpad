from pathlib import Path

import pytest


def _range_parser(text: str) -> list[int]:
    output = []
    text = text.replace(" ", "")
    items = text.split(",")
    for item in items:
        if "-" in item:
            start, stop = item.split("-")
            output.extend(list(range(int(start), int(stop) + 1)))
        else:
            output.append(int(item))
    return output


def _overlaps(first: set, second: set) -> bool:
    return any([
        first.issuperset(second),
        first.issubset(second),
        second.issuperset(first),
        second.issubset(first),
    ])


def _contains_any(first: set, second: set) -> bool:
    return any(item in second for item in first)


def part_one(values: list[tuple[set[int], set[int]]]) -> int:
    total = 0
    for first, second in values:
        if _overlaps(first, second):
            total += 1
    return total


def part_two(values: list[tuple[set[int], set[int]]]) -> int:
    total = 0
    for first, second in values:
        if _contains_any(first, second):
            total += 1
    return total


if __name__ == "__main__":
    data = [
        (set(_range_parser(item.split(",")[0])), set(_range_parser(item.split(",")[1])))
        for item in Path("../../../input.txt").read_text().strip().split("\n")

    ]
    print(part_one(values=data))
    print(part_two(values=data))


@pytest.mark.parametrize(
    "value,result",
    [
        ("2-4,6-8", False),
        ("2-3,4-5", False),
        ("5-7,7-9", False),
        ("2-8,3-7", True),
        ("6-6,4-6", True),
        ("2-6,4-8", False),
    ],
)
def test_part_one(value: str, result: bool):
    first, second = value.split(",")
    first, second = set(_range_parser(first)), set(_range_parser(second))
    assert _overlaps(first, second) == result


@pytest.mark.parametrize(
    "value,result",
    [
        ("2-4,6-8", False),
        ("2-3,4-5", False),
        ("5-7,7-9", True),
        ("2-8,3-7", True),
        ("6-6,4-6", True),
        ("2-6,4-8", True),
    ],
)
def test_part_two(value: str, result: bool):
    first, second = value.split(",")
    first, second = set(_range_parser(first)), set(_range_parser(second))
    assert _contains_any(first, second) == result
