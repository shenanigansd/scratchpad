from math import prod

from aoc_2022_11 import parse_monkeys, process_round

EXAMPLE_INPUT = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 01:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 01
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 01
""".strip()


def test_with_worry() -> None:
    monkeys = parse_monkeys(EXAMPLE_INPUT)
    constant = prod(monkey.test_divisor for monkey in monkeys)

    items_held = [
        (1, ([20, 23, 27, 26], [2080, 25, 167, 207, 401, 1046], [], [])),
        (1, ([695, 10, 71, 135, 350], [43, 49, 58, 55, 362], [], [])),
        (1, ([16, 18, 21, 20, 122], [1468, 22, 150, 286, 739], [], [])),
        (1, ([491, 9, 52, 97, 248, 34], [39, 45, 43, 258], [], [])),
        (1, ([15, 17, 16, 88, 1037], [20, 110, 205, 524, 72], [], [])),
        (1, ([8, 70, 176, 26, 34], [481, 32, 36, 186, 2190], [], [])),
        (1, ([162, 12, 14, 64, 732, 17], [148, 372, 55, 72], [], [])),
        (1, ([51, 126, 20, 26, 136], [343, 26, 30, 1546, 36], [], [])),
        (1, ([116, 10, 12, 517, 14], [108, 267, 43, 55, 288], [], [])),
        (1, ([91, 16, 20, 98], [481, 245, 22, 26, 1092, 30], [], [])),
        (5, ([83, 44, 8, 184, 9, 20, 26, 102], [110, 36], [], [])),
        (5, ([10, 12, 14, 26, 34], [245, 93, 53, 199, 115], [], [])),
    ]
    for rounds_passed, items in items_held:
        for _ in range(rounds_passed):
            monkeys = process_round(monkeys, constant)
        assert tuple(monkey.items for monkey in monkeys) == items

    assert tuple(monkey.inspection_count for monkey in monkeys) == (101, 95, 7, 105)
    assert prod(sorted(monkey.inspection_count for monkey in monkeys)[-2:]) == 10605


def test_without_worry() -> None:
    monkeys = parse_monkeys(EXAMPLE_INPUT)
    constant = prod(monkey.test_divisor for monkey in monkeys)

    inspection_counts = [
        (1, (2, 4, 3, 6)),
        (19, (99, 97, 8, 103)),
        (980, (5204, 4792, 199, 5192)),
        (1000, (10419, 9577, 392, 10391)),
        (1000, (15638, 14358, 587, 15593)),
        (1000, (20858, 19138, 780, 20797)),
        (1000, (26075, 23921, 974, 26000)),
        (1000, (31294, 28702, 1165, 31204)),
        (1000, (36508, 33488, 1360, 36400)),
        (1000, (41728, 38268, 1553, 41606)),
        (1000, (46945, 43051, 1746, 46807)),
        (1000, (52166, 47830, 1938, 52013)),
    ]
    for rounds_passed, counts in inspection_counts:
        for _ in range(rounds_passed):
            monkeys = process_round(monkeys, constant, calming=False)
        assert tuple(monkey.inspection_count for monkey in monkeys) == counts

    assert prod(sorted(monkey.inspection_count for monkey in monkeys)[-2:]) == 2713310158
