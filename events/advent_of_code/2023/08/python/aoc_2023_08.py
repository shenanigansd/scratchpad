import re
from itertools import cycle
from pathlib import Path


def parse_map(text: str) -> dict[str, tuple[str, str]]:
    return {
        group[0]: (group[1], group[2])
        for line in text.split("\n")
        for group in re.findall(r"(\w+) = \((\w+), (\w+)\)", line)
    }


def part1(directions: str, map_: dict[str, tuple[str, str]]) -> int:
    current_node = "AAA"
    for steps_taken, direction in enumerate(cycle(directions)):
        if direction == "L":
            current_node = map_[current_node][0]
        elif direction == "R":
            current_node = map_[current_node][1]
        else:
            msg = f"Unknown direction {direction}"
            raise ValueError(msg)
        if current_node == "ZZZ":
            return steps_taken
    return None


def part2(directions: str, map_: dict[str, tuple[str, str]]) -> int:
    nodes = [key for key in map_ if key.endswith("A")]
    for steps_taken, direction in enumerate(cycle(directions)):
        for index in range(len(nodes)):
            if direction == "L":
                nodes[index] = map_[nodes[index]][0]
            elif direction == "R":
                nodes[index] = map_[nodes[index]][1]
            else:
                msg = f"Unknown direction {direction}"
                raise ValueError(msg)
        if all(node.endswith("Z") for node in nodes):
            return steps_taken
    return None


if __name__ == "__main__":
    raw_text = Path("../input.txt").read_text()
    directions, map_ = raw_text.split("\n\n")
    map_ = parse_map(map_)
    print(part1(directions, map_))
    print(part2(directions, map_))
