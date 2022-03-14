#!/usr/bin/env python

from collections import defaultdict


def parse_input(values: list[str]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    output = []
    for value in values:
        left, right = value.split(" -> ")
        left_x, left_y = left.split(",")
        right_x, right_y = right.split(",")
        output.append(((int(left_x), int(left_y)), (int(right_x), int(right_y))))

    return output


def solve(values: list[tuple[tuple[int, int], tuple[int, int]]], include_diagonals: bool) -> int:
    lst = []
    for value in values:
        x1, y1 = value[0]
        x2, y2 = value[1]

        if x1 > x2:
            greater_x, smaller_x = x1, x2
        else:
            greater_x, smaller_x = x2, x1

        if y1 > y2:
            greater_y, smaller_y = y1, y2
        else:
            greater_y, smaller_y = y2, y1

        if smaller_x == greater_x:
            for y in range(smaller_y, greater_y + 1):
                lst.append((smaller_x, y))
        elif smaller_y == greater_y:
            for x in range(smaller_x, greater_x + 1):
                lst.append((x, smaller_y))
        elif include_diagonals:
            loop_x, loop_y = value[0]
            target_x, target_y = value[1]
            lst.append((target_x, target_y))
            while loop_x != target_x and loop_y != target_y:
                lst.append((loop_x, loop_y))
                loop_x += +1 if loop_x < target_x else -1
                loop_y += +1 if loop_y < target_y else -1

    dct = defaultdict(int)
    for value in lst:
        dct[value] += 1
    return sum(1 for value in dct.values() if value >= 2)


def part_one(values: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return solve(values, include_diagonals=False)


def part_two(values: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return solve(values, include_diagonals=True)


if __name__ == '__main__':
    values_: list[tuple[tuple[int, int], tuple[int, int]]] = parse_input(open("../../input.txt").readlines())
    print(part_one(values=values_))
    print(part_two(values=values_))
