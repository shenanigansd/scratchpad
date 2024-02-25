from pathlib import Path


def _find_unique_sequence(text: str, length: int) -> int | None:
    for index in range(length - 1, len(text)):
        if len(set(text[index - length : index])) == length:
            return index
    return None


def part_one(text: str) -> int:
    return _find_unique_sequence(text, 4)


def part_two(text: str) -> int:
    return _find_unique_sequence(text, 14)


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    print(part_one(data))
    print(part_two(data))
