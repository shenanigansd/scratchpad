import operator
from dataclasses import dataclass, field
from datetime import datetime
from math import floor, prod
from pathlib import Path

from parse import parse

operator_functions = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}

MONKEY_TEMPLATE = """\
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
    operation_function: operator
    operation_number: int | None
    test_divisor: int
    true_monkey: int
    false_monkey: int
    inspection_count: int = field(default=0)

    @classmethod
    def build_from(
        cls,
        *,
        monkey_id: int,
        starting_items: str,
        true_monkey: int,
        operation_sign: str,
        operation_number: int | None,
        test_divisor: int,
        false_monkey: int,
    ):
        items = [int(item) for item in starting_items.split(", ")]
        try:
            operation_number = int(operation_number)
        except ValueError:
            operation_number = None
        operation_function = operator_functions[operation_sign]
        return cls(
            monkey_id,
            items,
            operation_function,
            operation_number,
            test_divisor,
            true_monkey,
            false_monkey,
        )


def parse_monkeys(text: str) -> list[Monkey]:
    monkeys = []
    for monkey_text in text.split("\n\n"):
        monkey_kwargs = {}
        for template_line, text_line in zip(MONKEY_TEMPLATE.split("\n"), monkey_text.split("\n")):
            result = parse(template_line, text_line)
            monkey_kwargs.update(result.named)
        monkeys.append(Monkey.build_from(**monkey_kwargs))
    return monkeys


def process_round(monkeys: list[Monkey], worried: bool = True) -> list[Monkey]:
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey.inspection_count += 1
            item = monkey.items.pop(0)
            # print(f"got first {item}")
            item = monkey.operation_function(item, monkey.operation_number or item)
            # print(f"ran action, now {item}")
            if worried:
                item = floor(item / 3)
            # print(f"worried, now {item}")
            if item % monkey.test_divisor == 0:
                new_monkey = monkey.true_monkey
            else:
                new_monkey = monkey.false_monkey
            assert monkeys[new_monkey].monkey_id == new_monkey
            monkeys[new_monkey].items.append(item)
            # print(f"threw to {new_monkey}")
            # print("-" * 5)
    return monkeys


def part_one(text: str) -> int:
    monkeys = parse_monkeys(text)
    for _ in range(20):
        monkeys = process_round(monkeys)
    return prod(list(sorted(monkey.inspection_count for monkey in monkeys))[-2:])


def part_two(text: str) -> int:
    monkeys = parse_monkeys(text)
    for index in range(10000):
        print(datetime.now().time(), index)
        monkeys = process_round(monkeys, worried=False)
    return prod(list(sorted(monkey.inspection_count for monkey in monkeys))[-2:])


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    print(part_one(data))
    print(part_two(data))
