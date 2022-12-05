from collections import defaultdict


def part_one(movements: list[str]) -> int:
    delivered_presets = defaultdict(int)
    current_x, current_y = 0, 0
    delivered_presets[(current_x, current_y)] += 1
    for movement in movements:
        match movement:
            case "^":
                current_y += 1
            case "v":
                current_y -= 1
            case "<":
                current_x -= 1
            case ">":
                current_x += 1
        delivered_presets[(current_x, current_y)] += 1
    return len(delivered_presets.keys())


def part_two(movements: list[str]) -> int:
    delivered_presets = defaultdict(int)
    santa_x, santa_y = 0, 0
    robot_x, robot_y = 0, 0
    delivered_presets[(0, 0)] += 2
    for index, movement in enumerate(movements):
        diff_x, diff_y = 0, 0
        match movement:
            case "^":
                diff_y += 1
            case "v":
                diff_y -= 1
            case "<":
                diff_x -= 1
            case ">":
                diff_x += 1
        if index % 2 == 0:
            santa_x += diff_x
            santa_y += diff_y
            delivered_presets[(santa_x, santa_y)] += 1
        else:
            robot_x += diff_x
            robot_y += diff_y
            delivered_presets[(robot_x, robot_y)] += 1
    return len(delivered_presets.keys())


if __name__ == "__main__":
    lines: list[str] = open("../../../input.txt").readlines()
    data: list[str] = list(lines[0])

    print(part_one(movements=data))
    print(part_two(movements=data))
