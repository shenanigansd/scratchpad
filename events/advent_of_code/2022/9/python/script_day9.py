from dataclasses import dataclass, field
from enum import Enum, auto
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


@dataclass
class Rope:
    head: tuple[int, int]
    tail: tuple[int, int]
    tail_visited: list[tuple[int, int]] = field(default_factory=lambda: [(0, 0)])

    def move(self, movement: Movement) -> tuple[int, int]:
        print(f"{movement=}")
        for _ in range(movement.steps):
            print(f"before    \t{self.head=}\t{self.tail=}")
            self._move_head(movement.direction)
            print(f"moved head\t{self.head=}\t{self.tail=}")
            output = self._move_tail()
            print(f"moved tail\t{self.head=}\t{self.tail=}")
            print("-" * 20)
        return output

    def _move_head(self, direction: Direction) -> None:
        x_diff, y_diff = _move_one(direction)
        self.head = (self.head[0] + x_diff, self.head[1] + y_diff)

    def _tail_is_two_steps_away(self) -> Direction | None:
        x_diff = self.head[0] - self.tail[0]
        y_diff = self.head[1] - self.tail[1]
        if x_diff == +2:
            return Direction.RIGHT
        if x_diff == -2:
            return Direction.LEFT
        if y_diff == +2:
            return Direction.UP
        if y_diff == -2:
            return Direction.DOWN
        return None

    def _move_tail_straight(self, direction: Direction) -> tuple[int, int]:
        x_diff, y_diff = _move_one(direction)
        print(f"moved stai\t{x_diff=},{y_diff=}")
        self.tail = (self.tail[0] + x_diff, self.tail[1] + y_diff)
        self.tail_visited.append(self.tail)
        return self.tail

    def _tail_needs_diagonal_move(self) -> bool:
        return all([
            self.head[0] != self.tail[0],
            self.head[1] != self.tail[1],
        ])

    def _move_tail_diagonal(self) -> tuple[int, int]:
        x_diff = self.head[0] - self.tail[0]
        y_diff = self.head[1] - self.tail[1]

        if abs(x_diff) == abs(y_diff) == 1:
            return 0, 0  # exactly one off

        x_move = 1 if x_diff > 0 else -1
        y_move = 1 if y_diff > 0 else -1

        print(f"moved daig\t{x_move=},{y_move=}")
        self.tail = (self.tail[0] + x_move, self.tail[1] + y_move)
        self.tail_visited.append(self.tail)
        return self.tail

    def _move_tail(self) -> tuple[int, int]:
        output = 0, 0
        if self._tail_needs_diagonal_move():
            output = self._move_tail_diagonal()

        step_direction = self._tail_is_two_steps_away()
        if step_direction is not None:
            output = self._move_tail_straight(step_direction)

        return output


def part_one(movements: list[Movement]) -> int:
    rope = Rope(head=(0, 0), tail=(0, 0))
    for movement in movements:
        rope.move(movement)
    return len(set(rope.tail_visited))


def part_two(movements: list[Movement]) -> int:
    ropes = []
    for _ in range(10):
        ropes.append(Rope(head=(0, 0), tail=(0, 0)))
    for movement in movements:
        tail_position = ropes[0].move(movement)
        for rope in ropes[1:]:
            rope.head = tail_position
            rope._move_tail()
    return len(set(ropes[-1].tail_visited))


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    movements_ = [Movement.build_from(line) for line in data.splitlines()]
    print(part_one(movements_))
    print(part_two(movements_))
