def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


class Cell:
    def __init__(self, number: int):
        self.called = False
        self.number = number

    def __str__(self) -> str:
        if self.called:
            return f"({self.number})"
        else:
            return f"{self.number}"


class Row:
    def __init__(self, numbers: list[int]):
        self.cells: list[Cell] = [Cell(number=number) for number in numbers]

    def __str__(self) -> str:
        return " ".join(str(cell) for cell in self.cells)


class Board:
    def __init__(self, rows: list[list[int]]):
        self.rows: list[Row] = [Row(row) for row in rows]
        self.is_won = False

    def mark_number(self, called_number: int) -> bool:
        if self.is_won:
            return False

        for row in self.rows:
            for cell in row.cells:
                if cell.number == called_number:
                    cell.called = True
                    return True
        return False

    def check_win(self) -> bool:
        if self.is_won:
            return True
        rows = self.rows + self.get_columns()
        if any(all(cell.called is True for cell in row.cells) for row in rows):
            self.is_won = True
            return True
        return False

    def get_columns(self) -> list[Row]:
        output: list[Row] = []
        for index in range(len(self.rows[0].cells)):
            row = Row([])
            row.cells = [row.cells[index] for row in self.rows]
            output.append(row)

        return output

    def get_all_cells(self) -> list[Cell]:
        return [cell for row in self.rows for cell in row.cells]

    def __str__(self) -> str:
        return "\n".join(str(row) for row in self.rows)


def part_one(called_numbers: list[int], boards: list[Board]) -> int:
    for called_number in called_numbers:
        for board in boards:
            if board.mark_number(called_number):
                if board.check_win():
                    print(board)
                    return sum(cell.number for cell in board.get_all_cells() if cell.called is False) * called_number


def part_two(called_numbers: list[int], boards: list[Board]) -> int:
    winning_boards = {}

    for called_number in called_numbers:
        for board in boards:
            if board.mark_number(called_number):
                if board.check_win():
                    winning_boards[called_number] = board

    winning_number, winning_board = list(winning_boards.keys())[-1], list(winning_boards.values())[-1]
    return sum(cell.number for cell in winning_board.get_all_cells() if cell.called is False) * winning_number


if __name__ == '__main__':
    values_: list[str] = open("../../../input.txt").readlines()
    called_numbers_ = [int(val) for val in values_[0].split(",")]

    board_values = [rows[1:] for rows in chunks(values_[1:], 6)]
    boards_ = [Board([[int(val) for val in row.split()] for row in rows]) for rows in board_values]

    print(part_one(called_numbers=called_numbers_, boards=boards_))
    print(part_two(called_numbers=called_numbers_, boards=boards_))
