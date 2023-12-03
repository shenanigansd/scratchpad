from pathlib import Path


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


def count_adjacent_symbols(
    grid: list[list[str]],
    row_index: int,
    column_start_index: int,
    column_stop_index: int,
) -> int:
    total = 0

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
            total += 1
        if not is_last_row and is_symbol(grid[row_index + 1][column_index]):
            total += 1

    if is_symbol(grid[row_index][column_start_index + 1]):
        total += 1
    if is_symbol(grid[row_index][column_stop_index - 1]):
        total += 1

    return total


def sum_part_numbers_in_grid(grid: list[list[str]]) -> int:
    total = 0
    number_started_on = None
    for row_index in range(len(grid)):
        for column_index in range(len(grid[row_index])):
            if grid[row_index][column_index].isdigit():
                if number_started_on is None:
                    number_started_on = column_index
            else:
                if number_started_on is not None:
                    symbol_count = count_adjacent_symbols(grid, row_index, number_started_on, column_index)
                    if symbol_count > 0:
                        total += int("".join(grid[row_index][number_started_on:column_index]))
                    number_started_on = None
    return total


if __name__ == "__main__":
    raw_rows = Path("../input.txt").read_text().split("\n")
    grid = [list(row) for row in raw_rows]
    print(sum_part_numbers_in_grid(grid))
