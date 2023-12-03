from collections import defaultdict
from pathlib import Path


def is_symbol(char: str) -> bool:
    return not char.isdecimal() and char != "."


def find_adjacent_symbols(
    grid: list[list[str]],
    row_index: int,
    column_start_index: int,
    column_stop_index: int,
) -> dict[str, list[tuple[int, int]]]:
    adjacent_symbols = defaultdict(list)

    is_first_row = row_index == 0
    is_last_row = row_index == len(grid) - 1
    is_first_column = column_start_index == 0
    is_last_column = column_stop_index == len(grid[row_index]) - 1

    if not is_first_column:
        column_start_index -= 1
    if not is_last_column:
        column_stop_index += 1

    for column_index in range(column_start_index, column_stop_index + 1):
        if not is_first_row and is_symbol(grid[row_index - 1][column_index]):
            adjacent_symbols[grid[row_index - 1][column_index]].append((row_index - 1, column_index))
        if not is_last_row and is_symbol(grid[row_index + 1][column_index]):
            adjacent_symbols[grid[row_index + 1][column_index]].append((row_index + 1, column_index))

    if is_symbol(grid[row_index][column_start_index]):
        adjacent_symbols[grid[row_index][column_start_index]].append((row_index, column_start_index))
    if is_symbol(grid[row_index][column_stop_index]):
        adjacent_symbols[grid[row_index][column_stop_index]].append((row_index, column_stop_index))

    return adjacent_symbols


def find_part_numbers_in_grid(grid: list[list[str]]) -> dict[int, dict[str, list[tuple[int, int]]]]:
    part_numbers = {}
    for row_index in range(len(grid)):
        number_started_on = None
        number_ended_on = None
        for column_index in range(len(grid[row_index])):
            if grid[row_index][column_index].isdecimal() and number_started_on is None:
                number_started_on = column_index
            if number_started_on is not None:
                if not grid[row_index][column_index].isdecimal():
                    number_ended_on = column_index - 1
                elif (column_index + 1) == len(grid[row_index]):
                    number_ended_on = column_index
                if number_started_on is not None and number_ended_on is not None:
                    number = int("".join(grid[row_index][number_started_on : number_ended_on + 1]))
                    symbols_adjacent_to_number = find_adjacent_symbols(
                        grid,
                        row_index,
                        number_started_on,
                        number_ended_on,
                    )
                    part_numbers[number] = dict(symbols_adjacent_to_number)
                    number_started_on = None
                    number_ended_on = None
    return part_numbers


def sum_part_numbers_in_grid(grid: list[list[str]]) -> int:
    part_numbers = find_part_numbers_in_grid(grid)
    return sum(part_number for part_number in part_numbers if len(part_numbers[part_number]) > 0)


def sum_gears_in_grid(grid: list[list[str]]) -> int:
    part_numbers = find_part_numbers_in_grid(grid)
    total = 0
    seen = {}
    for part_number in part_numbers:
        if "*" in part_numbers[part_number]:
            for index in part_numbers[part_number]["*"]:
                if index in seen:
                    total += seen[index] * part_number
                seen[index] = part_number
    return total


def part1(grid: list[list[str]]) -> int:
    return sum_part_numbers_in_grid(grid)


def part2(grid: list[list[str]]) -> int:
    return sum_gears_in_grid(grid)


if __name__ == "__main__":
    raw_rows = Path("../input.txt").read_text().split("\n")
    grid = [list(row) for row in raw_rows]
    print(part1(grid))
    print(part2(grid))
