"""Advent of Code 2015 Day 2."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Box:
    """A box with length, width, and height."""

    length: int
    width: int
    height: int

    def sides_by_length(self) -> list[int]:
        """Return the sides of the box sorted by length."""
        return sorted([self.length, self.width, self.height])


def sum_needed_wrapping_paper(boxes: list[Box]) -> int:
    """Sum the total amount of wrapping paper needed."""
    total = 0
    for box in boxes:
        sides = (
            box.length * box.width,
            box.width * box.height,
            box.height * box.length,
        )
        smallest_side = min(sides)
        total += sum(sides) * 2 + smallest_side
    return total


def sum_needed_ribbon(boxes: list[Box]) -> int:
    """Sum the total amount of ribbon needed."""
    total = 0
    for box in boxes:
        total += sum(box.sides_by_length()[0:2]) * 2 + box.length * box.width * box.height
    return total


if __name__ == "__main__":
    lines: list[str] = Path("../input.txt").read_text().split("\n")
    boxes_: list[Box] = [Box(*map(int, line.split("x"))) for line in lines]

    print(sum_needed_wrapping_paper(boxes=boxes_))
    print(sum_needed_ribbon(boxes=boxes_))
