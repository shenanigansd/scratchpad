"""Advent of Code 2015 Day 1."""

from pathlib import Path


def find_final_floor(text: str) -> int:
    """Find the floor Santa ends up on.

    All we need is the final floor, so we can just count the number of open and close parentheses.
    """
    return sum(1 if char == "(" else -1 for char in text)


def find_when_santa_enters_basement(text: str) -> int:
    """Find the position of the first character that causes Santa to enter the basement.

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
    data = Path("../input.txt").read_text(encoding="locale")
    print(find_final_floor(text=data))
    print(find_when_santa_enters_basement(text=data))
