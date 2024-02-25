import operator
from collections.abc import Callable
from dataclasses import dataclass, field
from math import floor, prod
from pathlib import Path
from typing import Final, Self

from parse import parse

OPERATOR_FUNCTIONS: Final[dict[str, Callable]] = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}

MONKEY_TEMPLATE: Final[str] = """\
Monkey {monkey_id:d}:
  Starting items: {starting_items}
  Operation: new = old {operation_sign} {operation_number}
  Test: divisible by {test_divisor:d}
    If true: throw to monkey {true_monkey:d}
    If false: throw to monkey {false_monkey:d}
"""


@dataclass
class Monkey:
    monkey_id: int
    items: list[int]
    operation_function: Callable
    operation_number: int | None
    test_divisor: int
    true_monkey: int
    false_monkey: int
    inspection_count: int = field(default=0)

    @classmethod
    def build_from(  # noqa: PLR0913
        cls,
        *,
        monkey_id: int,
        starting_items: str,
        true_monkey: int,
        operation_sign: str,
        operation_number: int | None,
        test_divisor: int,
        false_monkey: int,
    ) -> Self:
        items = [int(item) for item in starting_items.split(", ")]
        try:
            operation_number = int(operation_number)
        except ValueError:
            operation_number = None
        operation_function = OPERATOR_FUNCTIONS[operation_sign]
        return cls(
            monkey_id,
            items,
            operation_function,
            operation_number,
            test_divisor,
            true_monkey,
            false_monkey,
        )


def parse_monkey(text: str) -> Monkey:
    monkey_kwargs = {}
    for template_line, text_line in zip(
        MONKEY_TEMPLATE.split("\n"),
        text.split("\n"),
        strict=False,
    ):
        result = parse(template_line, text_line)
        monkey_kwargs.update(result.named)
    return Monkey.build_from(**monkey_kwargs)


def parse_monkeys(text: str) -> list[Monkey]:
    return [parse_monkey(monkey_text) for monkey_text in text.split("\n\n")]


def process_round(
    monkeys: list[Monkey],
    constant: int,
    calming: bool = True,  # noqa: FBT001,FBT002
) -> list[Monkey]:
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey.inspection_count += 1
            item = monkey.items.pop(0)
            item = (
                monkey.operation_function(item, monkey.operation_number or item)
                % constant
            )
            if calming:
                item = floor(item / 3)
            if item % monkey.test_divisor == 0:
                new_monkey = monkey.true_monkey
            else:
                new_monkey = monkey.false_monkey
            assert monkeys[new_monkey].monkey_id == new_monkey
            monkeys[new_monkey].items.append(item)
    return monkeys


def process_rounds(monkeys: list[Monkey], rounds: int, calming: bool = True) -> int:  # noqa: FBT001,FBT002
    constant = prod(monkey.test_divisor for monkey in monkeys)
    for _ in range(rounds):
        monkeys = process_round(monkeys, constant, calming)
    return prod(sorted(monkey.inspection_count for monkey in monkeys)[-2:])


def part_one(text: str) -> int:
    monkeys = parse_monkeys(text)
    return process_rounds(monkeys, 20)


def part_two(text: str) -> int:
    monkeys = parse_monkeys(text)
    return process_rounds(monkeys, 10000, calming=False)


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    print(part_one(data))
    print(part_two(data))
