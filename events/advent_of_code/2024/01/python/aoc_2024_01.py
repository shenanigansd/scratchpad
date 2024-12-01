from collections import Counter
from pathlib import Path


def parse_input(text: str) -> tuple[list[int], list[int]]:
    rows = text.strip().split("\n")

    left = []
    right = []
    for row in rows:
        left_str, right_str = row.split()
        left.append(int(left_str))
        right.append(int(right_str))
    left.sort()
    right.sort()
    return left, right


def part1(left: list[int], right: list[int]) -> int:
    return sum(abs(left[index] - right[index]) for index in range(len(left)))


def part2(left: list[int], right: list[int]) -> int:
    right_counter = Counter(right)
    return sum(left_number * right_counter[left_number] for left_number in left)


if __name__ == "__main__":
    rows = Path("../input.txt").read_text(encoding="locale")
    print(part1(*parse_input(rows)))
    print(part2(*parse_input(rows)))
