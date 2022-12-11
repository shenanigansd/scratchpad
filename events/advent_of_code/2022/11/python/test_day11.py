from math import prod

from script_day11 import parse_monkeys, process_round

EXAMPLE_INPUT = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip()


def test_with_worry() -> None:
    monkeys = parse_monkeys(EXAMPLE_INPUT)

    # Round 1
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 2
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [695, 10, 71, 135, 350]
    assert monkeys[1].items == [43, 49, 58, 55, 362]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 3
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [16, 18, 21, 20, 122]
    assert monkeys[1].items == [1468, 22, 150, 286, 739]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 4
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [491, 9, 52, 97, 248, 34]
    assert monkeys[1].items == [39, 45, 43, 258]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 5
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [15, 17, 16, 88, 1037]
    assert monkeys[1].items == [20, 110, 205, 524, 72]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 6
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [8, 70, 176, 26, 34]
    assert monkeys[1].items == [481, 32, 36, 186, 2190]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 7
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [162, 12, 14, 64, 732, 17]
    assert monkeys[1].items == [148, 372, 55, 72]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 8
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [51, 126, 20, 26, 136]
    assert monkeys[1].items == [343, 26, 30, 1546, 36]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 9
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [116, 10, 12, 517, 14]
    assert monkeys[1].items == [108, 267, 43, 55, 288]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    # Round 10
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [91, 16, 20, 98]
    assert monkeys[1].items == [481, 245, 22, 26, 1092, 30]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    for _ in range(4):
        monkeys = process_round(monkeys)

    # Round 15
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [83, 44, 8, 184, 9, 20, 26, 102]
    assert monkeys[1].items == [110, 36]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    for _ in range(4):
        monkeys = process_round(monkeys)

    # Round 20
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkeys[1].items == [245, 93, 53, 199, 115]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    assert monkeys[0].inspection_count == 101
    assert monkeys[1].inspection_count == 95
    assert monkeys[2].inspection_count == 7
    assert monkeys[3].inspection_count == 105

    assert prod(list(sorted(monkey.inspection_count for monkey in monkeys))[-2:]) == 10605


def test_without_worry() -> None:
    monkeys = parse_monkeys(EXAMPLE_INPUT)

    monkeys = process_round(monkeys, worried=False)
    assert monkeys[0].inspection_count == 2
    assert monkeys[1].inspection_count == 4
    assert monkeys[2].inspection_count == 3
    assert monkeys[3].inspection_count == 6

    for _ in range(19):
        monkeys = process_round(monkeys, worried=False)
    # Round 20
    assert monkeys[0].inspection_count == 99
    assert monkeys[1].inspection_count == 97
    assert monkeys[2].inspection_count == 8
    assert monkeys[3].inspection_count == 103

    for _ in range(980):
        monkeys = process_round(monkeys, worried=False)
    # Round 1000
    assert monkeys[0].inspection_count == 5204
    assert monkeys[1].inspection_count == 4792
    assert monkeys[2].inspection_count == 199
    assert monkeys[3].inspection_count == 5192

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 2000
    assert monkeys[0].inspection_count == 10419
    assert monkeys[1].inspection_count == 9577
    assert monkeys[2].inspection_count == 392
    assert monkeys[3].inspection_count == 10391

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 3000
    assert monkeys[0].inspection_count == 15638
    assert monkeys[1].inspection_count == 14358
    assert monkeys[2].inspection_count == 587
    assert monkeys[3].inspection_count == 15593

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 4000
    assert monkeys[0].inspection_count == 20858
    assert monkeys[1].inspection_count == 19138
    assert monkeys[2].inspection_count == 780
    assert monkeys[3].inspection_count == 20797

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 5000
    assert monkeys[0].inspection_count == 26075
    assert monkeys[1].inspection_count == 23921
    assert monkeys[2].inspection_count == 974
    assert monkeys[3].inspection_count == 26000

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 6000
    assert monkeys[0].inspection_count == 31294
    assert monkeys[1].inspection_count == 28702
    assert monkeys[2].inspection_count == 1165
    assert monkeys[3].inspection_count == 31204

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 7000
    assert monkeys[0].inspection_count == 36508
    assert monkeys[1].inspection_count == 33488
    assert monkeys[2].inspection_count == 1360
    assert monkeys[3].inspection_count == 36400

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 8000
    assert monkeys[0].inspection_count == 41728
    assert monkeys[1].inspection_count == 38268
    assert monkeys[2].inspection_count == 1553
    assert monkeys[3].inspection_count == 41606

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 9000
    assert monkeys[0].inspection_count == 46945
    assert monkeys[1].inspection_count == 43051
    assert monkeys[2].inspection_count == 1746
    assert monkeys[3].inspection_count == 46807

    for _ in range(1000):
        monkeys = process_round(monkeys, worried=False)
    # Round 10000
    assert monkeys[0].inspection_count == 52166
    assert monkeys[1].inspection_count == 47830
    assert monkeys[2].inspection_count == 1938
    assert monkeys[3].inspection_count == 52013

    assert prod(list(sorted(monkey.inspection_count for monkey in monkeys))[-2:]) == 2713310158
