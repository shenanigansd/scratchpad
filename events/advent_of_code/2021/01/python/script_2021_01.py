def part_one(values: list[int]) -> int:
    count = sum(values[index] < values[index + 1] for index in range(len(values) - 1))
    return count


def part_two(values: list[int]) -> int:
    summed_list = list(sum(three) for three in zip(values, values[1:], values[2:]))
    count = sum(summed_list[index] < summed_list[index + 1] for index in range(len(summed_list) - 1))
    return count


if __name__ == "__main__":
    values_: list[int] = [int(row) for row in open("../input.txt").readlines()]
    print(part_one(values=values_))
    print(part_two(values=values_))
