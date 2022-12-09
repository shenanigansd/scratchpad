from dataclasses import dataclass
from enum import Enum, auto
from itertools import pairwise
from pathlib import Path


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


DIRECTION_MAP: dict[str, Direction] = {
    "L": Direction.LEFT,
    "R": Direction.RIGHT,
    "U": Direction.UP,
    "D": Direction.DOWN,
}


@dataclass(frozen=True, slots=True)
class Movement:
    direction: Direction
    steps: int

    @classmethod
    def build_from(cls, text: str) -> "Movement":
        direction_, steps_ = text.split()
        return cls(DIRECTION_MAP[direction_], int(steps_))


@dataclass(frozen=True, slots=True)
class Knot:
    x: int
    y: int


def _move_one(direction: Direction) -> tuple[int, int]:
    match direction:
        case Direction.UP:
            return 0, 1
        case Direction.DOWN:
            return 0, -1
        case Direction.LEFT:
            return -1, 0
        case Direction.RIGHT:
            return 1, 0


def knot_is_two_steps_away(previous: Knot, knot: Knot) -> Direction | None:
    x_diff = previous.x - knot.x
    y_diff = previous.y - knot.y
    if x_diff == +2:
        return Direction.RIGHT
    if x_diff == -2:
        return Direction.LEFT
    if y_diff == +2:
        return Direction.UP
    if y_diff == -2:
        return Direction.DOWN
    return None


def move_knot_straight(knot: Knot, direction: Direction) -> Knot:
    x_diff, y_diff = _move_one(direction)
    knot = Knot(knot.x + x_diff, knot.y + y_diff)
    return knot


def move_knot_diagonal(previous: Knot, knot: Knot) -> Knot:
    x_diff = previous.x - knot.x
    y_diff = previous.y - knot.y

    if abs(x_diff) == abs(y_diff) == 1:
        return knot  # exactly one off

    x_move = 1 if x_diff > 0 else -1
    y_move = 1 if y_diff > 0 else -1
    return Knot(knot.x + x_move, knot.y + y_move)


def move_knot(previous: Knot, knot: Knot) -> Knot:
    if all([
        previous.x != knot.x,
        previous.y != knot.y,
    ]):
        return move_knot_diagonal(previous, knot)

    step_direction = knot_is_two_steps_away(previous, knot)
    if step_direction is not None:
        return move_knot_straight(knot, step_direction)

    return knot


def run(knot_quantity: int, movements: list[Movement]) -> int:
    visited: set[Knot] = set()
    knots: list[Knot] = [Knot(0, 0) for _ in range(knot_quantity)]
    for movement in movements:
        for _ in range(movement.steps):
            x_diff, y_diff = _move_one(movement.direction)
            knots[0] = Knot(knots[0].x + x_diff, knots[0].y + y_diff)

            for index, (previous, knot) in enumerate(pairwise(knots)):
                knots[index] = move_knot(previous, knot)

            visited.add(knots[-1])
    return len(visited)


def part_one(movements: list[Movement]) -> int:
    return run(1, movements)


def part_two(movements: list[Movement]) -> int:
    return run(10, movements)


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    movements_ = [Movement.build_from(line) for line in data.splitlines()]
    print(part_one(movements_))
    print(part_two(movements_))
