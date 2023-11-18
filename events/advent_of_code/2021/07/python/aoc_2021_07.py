import statistics


def part_one(values: list[int]) -> int:
    median = statistics.median(values)
    return sum(abs(value - median) for value in values)


def part_two(values: list[int]) -> int:
    return min(
        sum(sum(1 + iteration for iteration in range(abs(value - iteration))) for value in values)
        for iteration in range(len(values))
    )


if __name__ == "__main__":
    values_: list[int] = [int(value) for value in open("../input.txt").readlines()[0].split(",")]
    print(part_one(values=values_.copy()))
    print(part_two(values=values_.copy()))
