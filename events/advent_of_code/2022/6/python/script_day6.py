from collections import Counter
from pathlib import Path


def _find_four_unique(text: str) -> int:
    for index in range(3, len(text)):
        if all(value == 1 for value in Counter(text[index - 3:index + 1]).values()):
            return index + 1


def _find_fourteen_unique(text: str) -> int:
    for index in range(13, len(text)):
        if all(value == 1 for value in Counter(text[index - 13:index + 1]).values()):
            return index + 1


def part_one(text: str) -> int:
    return _find_four_unique(text)


def part_two(text: str) -> int:
    return _find_fourteen_unique(text)


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    print(part_one(data))
    print(part_two(data))
