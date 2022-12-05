from pathlib import Path


def _range_parser(text: str) -> list[int]:
    output = []
    text = text.replace(" ", "")
    items = text.split(",")
    for item in items:
        if "-" in item:
            start, stop = item.split("-")
            output.extend(list(range(int(start), int(stop) + 1)))
        else:
            output.append(int(item))
    return output


def _overlaps(first: set, second: set) -> bool:
    return any(
        [
            first.issuperset(second),
            first.issubset(second),
            second.issuperset(first),
            second.issubset(first),
        ]
    )


def _contains_any(first: set, second: set) -> bool:
    return any(item in second for item in first)


def part_one(values: list[tuple[set[int], set[int]]]) -> int:
    total = 0
    for first, second in values:
        if _overlaps(first, second):
            total += 1
    return total


def part_two(values: list[tuple[set[int], set[int]]]) -> int:
    total = 0
    for first, second in values:
        if _contains_any(first, second):
            total += 1
    return total


if __name__ == "__main__":
    data = [
        (set(_range_parser(item.split(",")[0])), set(_range_parser(item.split(",")[1])))
        for item in Path("../../../input.txt").read_text().strip().split("\n")
    ]
    print(part_one(values=data))
    print(part_two(values=data))
