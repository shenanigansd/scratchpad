def part_one(values: list[int | None]) -> int:
    sums = []
    total = 0
    for value in values:
        if value is None:
            sums.append(total)
            total = 0
        else:
            total += value
    return max(sums)


def part_two(values: list[int]) -> int:
    sums = []
    total = 0
    for value in values:
        if value is None:
            sums.append(total)
            total = 0
        else:
            total += value
    return sum(sorted(sums)[-3:])


if __name__ == "__main__":
    with open("../../../input.txt") as file:
        values_: list[str] = file.readlines()
    values_: list[int | None] = [int(value) if value != "\n" else None for value in values_]
    print(part_one(values=values_))
    print(part_two(values=values_))
