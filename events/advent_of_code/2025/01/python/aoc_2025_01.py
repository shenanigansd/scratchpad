import enum
import operator
from pathlib import Path


class Direction(enum.Enum):
    LEFT = "L"
    RIGHT = "R"


def parse_input(text: str) -> list[tuple[Direction, int]]:
    values = text.strip().split("\n")

    output = []
    for value in values:
        direction_str, number_str = value[0], value[1:]
        direction = Direction(direction_str)
        number = int(number_str)
        output.append((direction, number))
    return output


def part1(movements: list[tuple[Direction, int]]) -> int:
    dial_position = 50
    times_dial_hit_zero = 0

    for direction, steps in movements:
        if direction == Direction.LEFT:
            dial_position -= steps
        elif direction == Direction.RIGHT:
            dial_position += steps

        while dial_position < 0:
            dial_position += 100
        while dial_position >= 100:
            dial_position -= 100

        if dial_position == 0:
            times_dial_hit_zero += 1

    return times_dial_hit_zero


def part2(movements: list[tuple[Direction, int]]) -> int:
    dial_position = 50
    times_dial_passed_zero = 0

    for direction, steps in movements:
        if direction == Direction.LEFT:
            function = operator.sub
        elif direction == Direction.RIGHT:
            function = operator.add

        for _ in range(steps):
            dial_position = function(dial_position, 1)

            if dial_position < 0:
                dial_position += 100
            elif dial_position >= 100:
                dial_position -= 100

            if dial_position == 0:
                times_dial_passed_zero += 1

    return times_dial_passed_zero


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    values = parse_input(text)
    print(part1(values))
    print(part2(values))
