from aoc_2024_04 import part1, part2

TEST_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def test_part1() -> None:
    assert part1(TEST_INPUT) == 18


def test_part2() -> None:
    assert part2(TEST_INPUT) == 0
