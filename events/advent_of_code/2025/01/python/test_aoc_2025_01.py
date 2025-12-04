from aoc_2025_01 import Direction, parse_input, part1, part2

TEST_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

PARSED_EXAMPLE = [
    (Direction.LEFT, 68),
    (Direction.LEFT, 30),
    (Direction.RIGHT, 48),
    (Direction.LEFT, 5),
    (Direction.RIGHT, 60),
    (Direction.LEFT, 55),
    (Direction.LEFT, 1),
    (Direction.LEFT, 99),
    (Direction.RIGHT, 14),
    (Direction.LEFT, 82),
]


def test_parse_input() -> None:
    assert parse_input(TEST_INPUT) == PARSED_EXAMPLE


def test_part1() -> None:
    assert part1(PARSED_EXAMPLE) == 3


def test_part2() -> None:
    assert part2(PARSED_EXAMPLE) == 6
