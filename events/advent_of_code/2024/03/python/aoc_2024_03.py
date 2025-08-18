import re
from math import prod
from pathlib import Path


def part1(text: str) -> int:
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text, re.MULTILINE))


def part2(text: str) -> int:
    do_indexes = [match.start(0) for match in re.finditer(r"do\(\)", text)]
    dont_indexes = [match.start(0) for match in re.finditer(r"don't\(\)", text)]
    map_ = [True] * len(text)
    in_do = True
    for counter in range(len(map_)):
        if counter in do_indexes:
            in_do = True
        elif counter in dont_indexes:
            in_do = False
        map_[counter] = in_do

    return sum(
        prod(map(int, match.groups()))
        for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", text, re.MULTILINE)
        if map_[match.start(0)]
    )


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    print(part1(text))
    print(part2(text))
