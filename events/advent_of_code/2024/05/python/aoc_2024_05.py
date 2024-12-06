from pathlib import Path


def parse_input(text: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    text = text.strip()
    left, right = text.split("\n\n")
    pairs = [tuple(map(int, line.split("|"))) for line in left.split("\n")]
    pages = [list(map(int, line.split(","))) for line in right.split("\n")]
    return pairs, pages


def part1(pairs: list[tuple[int, int]], pages: list[list[int]]) -> int:
    total = 0
    for page in pages:
        valid = True
        for pair in pairs:
            try:
                left_index = page.index(pair[0])
                right_index = page.index(pair[1])
                if right_index < left_index:
                    valid = False
                    break
            except ValueError:
                continue
        if valid:
            total += page[len(page) // 2]
    return total


def part2(pairs: list[tuple[int, int]], pages: list[list[int]]) -> int:
    total = 0
    invalid_pages: list[list[int]] = []
    for page in pages:
        valid = True
        for pair in pairs:
            try:
                left_index = page.index(pair[0])
                right_index = page.index(pair[1])
                if right_index < left_index:
                    valid = False
                    break
            except ValueError:
                continue
        if not valid:
            invalid_pages.append(page)

    for page in invalid_pages:
        for pair in pairs:
            try:
                left_index = page.index(pair[0])
                right_index = page.index(pair[1])
                if right_index < left_index:
                    page.remove(pair[1])
                    page.insert(left_index, pair[1])
            except ValueError:
                continue
    total += page[len(page) // 2]

    return total


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    print(part1(*parse_input(text)))
    print(part2(*parse_input(text)))
