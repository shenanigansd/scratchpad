from pathlib import Path


def is_periodic(text: str, length: int) -> bool:
    # must divide evenly
    if len(text) % length != 0:
        return False

    chunk = text[:length]
    return all(text[i:i + length] == chunk for i in range(0, len(text), length))


def parse_input(text: str) -> list[tuple[int, int]]:
    return [tuple(int(part) for part in range_str.split("-")) for range_str in text.split(",")]


def part1(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for start, end in ranges:
        for value in range(start, end + 1):
            text = str(value)
            midpoint = len(text) // 2
            if text[:midpoint] == text[midpoint:]:
                total += value
    return total


def part2(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for start, end in ranges:
        for value in range(start, end + 1):
            text = str(value)
            for length in range(1, len(text)):
                if is_periodic(text, length):
                    total += value
                    break
    return total


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    values = parse_input(text)
    print(part1(values))
    print(part2(values))
