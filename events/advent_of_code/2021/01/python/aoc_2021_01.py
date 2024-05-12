from pathlib import Path


def part_one(values: list[int]) -> int:
    return sum(values[index] < values[index + 1] for index in range(len(values) - 1))


def part_two(values: list[int]) -> int:
    summed_list = [sum(three) for three in zip(values, values[1:], values[2:], strict=False)]
    return sum(summed_list[index] < summed_list[index + 1] for index in range(len(summed_list) - 1))


if __name__ == "__main__":
    values_: list[int] = [int(row) for row in Path("../input.txt").read_text(encoding="locale").split("\n")]
    print(part_one(values=values_))
    print(part_two(values=values_))
