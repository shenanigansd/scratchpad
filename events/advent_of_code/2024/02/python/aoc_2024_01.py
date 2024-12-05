import collections
from collections.abc import Generator, Iterable
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any


def sliding_window(iterable: Iterable, n: int) -> Generator[tuple[Any, ...]]:
    """Collect data into overlapping fixed-length chunks or blocks."""
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = collections.deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


@dataclass(frozen=True)
class Report:
    values: list[int]

    def is_safe(self, *, dampener_enabled: bool = False) -> bool:
        dampener_used = False

        increasing_changes = sum(1 for left, right in zip(self.values, self.values[1:], strict=False) if left > right)
        if dampener_enabled and not dampener_used and increasing_changes == 1:
            dampener_used = True
            increasing_changes -= 1
        all_increasing = increasing_changes == 0

        decreasing_changes = sum(1 for left, right in zip(self.values, self.values[1:], strict=False) if left < right)
        if dampener_enabled and not dampener_used and decreasing_changes == 1:
            dampener_used = True
            decreasing_changes -= 1
        all_decreasing = decreasing_changes == 0

        unsafe_values = 0
        for left, right in sliding_window(self.values, 2):
            print(f"{left=}, {right=}, {abs(left - right)=}")
            if not 1 <= abs(left - right) <= 3:
                unsafe_values += 1
        print(f"{unsafe_values=}")
        if dampener_enabled and not dampener_used and unsafe_values == 1:
            dampener_used = True
            unsafe_values -= 1
        within_boundaries = unsafe_values == 0
        print(f"{within_boundaries=}")

        return (all_increasing or all_decreasing) and within_boundaries


def parse_input(text: str) -> list[Report]:
    reports = [list(map(int, row.split())) for row in text.strip().split("\n")]
    return [Report(values) for values in reports]


def part1(reports: list[Report]) -> int:
    return sum(report.is_safe() for report in reports)


def part2(reports: list[Report]) -> int:
    return sum(report.is_safe(dampener_enabled=True) for report in reports)


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    print(part1(parse_input(text)))
    print(part2(parse_input(text)))
