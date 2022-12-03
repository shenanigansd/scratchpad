from collections import Counter
from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

from darbia.utils.iterables import chunks, flatten

priorities = dict(zip(ascii_lowercase + ascii_uppercase, range(1, 52 + 1)))


def part_one(values: list[str]) -> int:
    total = 0
    for value in values:
        left, right = value[:len(value) // 2], value[len(value) // 2:]
        left, right = set(left), set(right)
        for character in left:
            if character in right:
                total += priorities[character]
    return total


def part_two(values: list[str]) -> int:
    total = 0
    for group in chunks(values, 3):
        counter = Counter(flatten([list(set(chunk)) for chunk in group]))
        for character, occurrences in counter.items():
            if occurrences == 3:
                total += priorities[character]
                break
    return total


if __name__ == '__main__':
    data = Path("../../../input.txt").read_text().split("\n")
    print(priorities)
    print(part_one(values=data))
    print(part_two(values=data))


def test_part_one():
    assert part_one([
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]) == 157


def test_part_two():
    assert part_two([
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    ]) == 18

    assert part_two([
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]) == 52
