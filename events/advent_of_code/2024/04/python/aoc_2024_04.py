import re
from math import prod
from pathlib import Path


LEFT_OFFSETS = [(0, -1), (0, -2), (0, -3), (0, -4)]
RIGHT_OFFSETS = [(0, 1), (0, 2), (0, 3), (0, 4)]
UP_OFFSETS = [(-1, 0), (-2, 0), (-3, 0), (-4, 0)]
DOWN_OFFSETS = [(1, 0), (2, 0), (3, 0), (4, 0)]
DIAGONAL_OFFSETS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
DIAGONAL_LEFT_UP_OFFSETS = [(-1, -1), (-2, -2), (-3, -3), (-4, -4)]
DIAGONAL_LEFT_DOWN_OFFSETS = [(1, -1), (2, -2), (3, -3), (4, -4)]
DIAGONAL_RIGHT_UP_OFFSETS = [(-1, 1), (-2, 2), (-3, 3), (-4, 4)]
DIAGONAL_RIGHT_DOWN_OFFSETS = [(1, 1), (2, 2), (3, 3), (4, 4)]

OFFSETS = {
    "left": LEFT_OFFSETS,
    "right": RIGHT_OFFSETS,
    "up": UP_OFFSETS,
    "down": DOWN_OFFSETS,
    "diagonal": DIAGONAL_OFFSETS,
    "diagonal_left_up": DIAGONAL_LEFT_UP_OFFSETS,
    "diagonal_left_down": DIAGONAL_LEFT_DOWN_OFFSETS,
    "diagonal_right_up": DIAGONAL_RIGHT_UP_OFFSETS,
    "diagonal_right_down": DIAGONAL_RIGHT_DOWN_OFFSETS,
}

def part1(text: str) -> int:
    text = text.lstrip("\n").rstrip("\n")
    count = 0
    grid = [list(line) for line in text.split("\n")]
    height = len(grid)
    width = len(grid[0])
    for y in range(height):
        for x in range(width):
            print(f"Checking {y}, {x}, {grid[y][x]}")            
            if grid[y][x] == "X":
                for offset_name,offsets in OFFSETS.items():
                    try:
                       if "".join([grid[y + offset[0]][x + offset[1]] for offset in offsets]) == "XMAS":
                        count += 1
                        print(f"Found XMAS at {y}, {x}, {offset_name}")
                    except IndexError:
                        continue
    return count


def part2(text: str) -> int:
    return 0


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    print(part1(text))
    print(part2(text))
