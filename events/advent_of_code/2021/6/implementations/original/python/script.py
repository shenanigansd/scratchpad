#!/usr/bin/env python

from collections import Counter


def simulate_day(state: list[int]) -> list[int]:
    new_state = [0 for _ in range(9)]
    new_babies = state[0]
    for i in range(1, 9):
        new_state[i - 1] = state[i]
    new_state[8] += new_babies
    new_state[6] += new_babies
    state = new_state

    return state


def part_one(values: list[int]) -> int:
    for _ in range(80):
        values = simulate_day(values)

    return sum(values)


def part_two(values: list[int]) -> int:
    for _ in range(256):
        values = simulate_day(values)

    return sum(values)


if __name__ == '__main__':
    values_: Counter = Counter([int(value) for value in open("../../../input.txt").readlines()[0].split(",")])
    values_: list[int] = [values_.get(i, 0) for i in range(9)]
    print(part_one(values=values_.copy()))
    print(part_two(values=values_.copy()))
