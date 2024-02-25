import re
from itertools import pairwise
from pathlib import Path

pat = r"(?=.*?(?:(.).\1))(?=.*?(.{2}).*?\2).*"


def _contains_any(text: str, values: list[str]) -> bool:
    return any(value in text for value in values)


def _contains_at_least_x_of(text: str, occurrences: int, values: list[str]) -> bool:
    return sum(text.count(value) for value in values) >= occurrences


def _contains_sequential_duplicate(text: str) -> bool:
    return any(current == nxt for current, nxt in pairwise(text))


def _contains_duplicate_with_buffer(text: str, buffer: int = 1) -> bool:
    return any(current == nxt for current, nxt in zip(text, text[buffer + 1 :], strict=False))


def _contains_non_overlapping_duplicate_sequence(text: str, length: int = 2) -> bool:
    for index in range(len(text)):
        if text.count(text[index : length + 1]) > 1 and len(text[index : length + 1].strip()) > 1:
            print(f"{text[index : length + 1]}\t{text.count(text[index : length + 1])}")
            return True
    return False


def part_one(values: list[str]) -> int:
    nice_strings = 0
    for value in values:
        conditions = (
            _contains_at_least_x_of(value, 3, list("aeiou")),
            _contains_sequential_duplicate(value),
            not _contains_any(value, ["ab", "cd", "pq", "xy"]),
        )
        if all(conditions):
            nice_strings += 1

    return nice_strings


def part_two(values: list[str]) -> int:
    nice_strings = 0
    for value in values:
        conditions = (
            _contains_non_overlapping_duplicate_sequence(value),
            _contains_duplicate_with_buffer(value),
        )
        if all(conditions):
            nice_strings += 1

        status = "GOOD" if all(conditions) != bool(re.match(pat, value)) else "\t\tBAD"
        print(f"{value=}\t{status}")

    return nice_strings


if __name__ == "__main__":
    data: list[str] = Path("../input.txt").read_text().strip().split("\n")

    print(part_one(values=data))
    print(part_two(values=data))
