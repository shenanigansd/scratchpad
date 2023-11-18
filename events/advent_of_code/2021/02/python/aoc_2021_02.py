def part_one(values: list[str]) -> int:
    horizontal_position = 0
    depth = 0

    for value in values:
        direction_, distance_ = value.split()
        match [direction_, int(distance_)]:
            case ["forward", distance]:
                horizontal_position += distance
            case ["down", distance]:
                depth += distance
            case ["up", distance]:
                depth -= distance

    return horizontal_position * depth


def part_two(values: list[str]) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for value in values:
        direction_, distance_ = value.split()
        match [direction_, int(distance_)]:
            case ["forward", distance]:
                horizontal_position += distance
                depth += distance * aim
            case ["down", distance]:
                aim += distance
            case ["up", distance]:
                aim -= distance

    return horizontal_position * depth


if __name__ == "__main__":
    values_: list[str] = [row for row in open("../input.txt").readlines()]
    print(part_one(values=values_))
    print(part_two(values=values_))
