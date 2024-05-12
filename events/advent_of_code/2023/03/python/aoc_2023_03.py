from pathlib import Path


def is_symbol(char: str) -> bool:
    return not char.isdecimal() and char != "."


def find_adjacent_symbol(
    grid: list[list[str]],
    row_index: int,
    column_start_index: int,
    column_stop_index: int,
) -> tuple[str, int, int] | None:
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
            return (grid[row_index - 1][column_index], row_index - 1, column_index)
        if not is_last_row and is_symbol(grid[row_index + 1][column_index]):
            return (grid[row_index + 1][column_index], row_index + 1, column_index)

    if is_symbol(grid[row_index][column_start_index]):
        return (grid[row_index][column_start_index], row_index, column_start_index)
    if is_symbol(grid[row_index][column_stop_index]):
        return (grid[row_index][column_stop_index], row_index, column_stop_index)

    return None


def find_part_numbers_in_grid(
    grid: list[list[str]],
) -> dict[tuple[int, int, int], tuple[str, int, int] | None]:
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
                    number = int(
                        "".join(
                            grid[row_index][number_started_on : number_ended_on + 1],
                        ),
                    )
                    part_numbers[(number, row_index, number_started_on)] = find_adjacent_symbol(
                        grid,
                        row_index,
                        number_started_on,
                        number_ended_on,
                    )
                    number_started_on = None
                    number_ended_on = None
    return part_numbers


def sum_part_numbers_in_grid(grid: list[list[str]]) -> int:
    part_numbers = find_part_numbers_in_grid(grid)
    return sum(part_number[0] for part_number in part_numbers if part_numbers[part_number] is not None)


def sum_gears_in_grid(grid: list[list[str]]) -> int:
    part_numbers = find_part_numbers_in_grid(grid)
    total = 0
    seen = {}
    for key_tuple, value_tuple in part_numbers.items():
        if value_tuple is None:
            continue
        indices = value_tuple[1:]
        if indices in seen:
            total += seen[indices] * key_tuple[0]
        seen[indices] = key_tuple[0]
    return total


def part1(grid: list[list[str]]) -> int:
    return sum_part_numbers_in_grid(grid)


def part2(grid: list[list[str]]) -> int:
    return sum_gears_in_grid(grid)


if __name__ == "__main__":
    raw_rows = Path("../input.txt").read_text(encoding="locale").split("\n")
    grid = [list(row) for row in raw_rows]
    print(part1(grid))
    print(part2(grid))
