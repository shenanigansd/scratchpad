from aoc_2023_03 import sum_part_numbers_in_grid

RAW_TEXT = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_parsing_data() -> None:
    grid = [list(row) for row in RAW_TEXT.strip().split("\n")]
    assert sum_part_numbers_in_grid(grid) == 4361
