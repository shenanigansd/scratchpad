"""Advent of Code 2015-01."""

from pathlib import Path


def part_one(text: str) -> int:
    """Return the floor Santa ends up on.

    All we need is the final floor, so we can just count the number of open and close parentheses.
    """
    return sum(1 if char == "(" else -1 for char in text)


def part_two(text: str) -> int:
    """Return the position of the first character that causes Santa to enter the basement.

    Now we need to keep track of the floor to know when Santa enters the basement.
    """
    floor = 0
    for index, char in enumerate(text, start=1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return index

    msg = "Santa never enters the basement!"
    raise ValueError(msg)


if __name__ == "__main__":
    data = Path("../input.txt").read_text()
    print(part_one(text=data))
    print(part_two(text=data))
