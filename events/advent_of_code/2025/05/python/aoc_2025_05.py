from pathlib import Path


def parse_input(text: str) -> tuple[list[range], list[int]]:
    range_text, ingredient_text = text.split("\n\n")
    range_numbers = [tuple(map(int, line.split("-"))) for line in range_text.split("\n") if line]
    ranges = [range(start, end + 1) for start, end in range_numbers]
    ingredient_ids = list(map(int, ingredient_text.split("\n")))
    return ranges, ingredient_ids


def part1(ranges: list[range], ingredient_ids: list[int]) -> int:
    return sum(1 for ingredient_id in ingredient_ids if any(ingredient_id in range_ for range_ in ranges))


def part2(ranges: list[range]) -> int:
    return len(set().union(list(range_) for range_ in ranges))


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    ranges, ingredient_ids = parse_input(text)
    print(part1(ranges, ingredient_ids))
    print(part2(ranges))
