"""Advent of Code 2015-01."""

from pathlib import Path


def part_one(text: str) -> int:
    """Return the floor number (part one)."""
    return sum(1 if char == "(" else -1 for char in text)


def part_two(text: str) -> int:
    """Return the position of the first character that causes Santa to enter the basement (part two)."""
    floor = 0
    for index, char in enumerate(text, start=1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            return index
    return None


if __name__ == "__main__":
    data = Path("../input.txt").read_text()
    print(part_one(text=data))
    print(part_two(text=data))
