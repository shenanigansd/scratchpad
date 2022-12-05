import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from darbia.utils.iterables import chunks


@dataclass(frozen=True)
class Movement:
    quantity: int
    from_stack: int
    to_stack: int


@dataclass
class Warehouse:
    stacks: dict[int, list[str]]

    @classmethod
    def build_from(cls, text: str) -> "Warehouse":
        header, *lines = list(reversed(text.splitlines()))
        stack_count = len(header.split())
        warehouse = Warehouse({index: [] for index in range(1, stack_count + 1)})
        for line in lines:
            stack = 1
            for chunk in chunks(line, 4):
                if chunk[0] == "[":
                    warehouse.stacks[stack].append(chunk[1])
                stack += 1
        return warehouse

    def move_single(self, movement: Movement) -> None:
        for _ in range(movement.quantity):
            self.stacks[movement.to_stack].append(
                self.stacks[movement.from_stack].pop()
            )

    def move_bulk(self, movement: Movement) -> None:
        crates_to_move = self.stacks[movement.from_stack][-movement.quantity :]
        self.stacks[movement.from_stack] = self.stacks[movement.from_stack][
            : -movement.quantity
        ]
        self.stacks[movement.to_stack].extend(crates_to_move)

    def tops(self) -> str:
        return "".join(stack[-1] for stack in self.stacks.values())


def part_one(warehouse: Warehouse, movements: Iterable[Movement]) -> str:
    for movement in movements:
        warehouse.move_single(movement)
    return warehouse.tops()


def part_two(warehouse: Warehouse, movements: Iterable[Movement]) -> str:
    for movement in movements:
        warehouse.move_bulk(movement)
    return warehouse.tops()


if __name__ == "__main__":
    warehouse_text, instructions = (
        Path("../input.txt").read_text().strip().split("\n\n")
    )
    movements_ = [
        Movement(
            *map(int, re.match(r"move (\d+) from (\d+) to (\d+)", instruction).groups())
        )
        for instruction in instructions.splitlines()
    ]

    print(part_one(Warehouse.build_from(warehouse_text), movements_))
    print(part_two(Warehouse.build_from(warehouse_text), movements_))
