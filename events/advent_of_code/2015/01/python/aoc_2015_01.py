from pathlib import Path


def part_one(text: str) -> int:
    return sum(1 if char == "(" else -1 for char in text)


def part_two(text: str) -> int:
    floor = 0
    for index, char in enumerate(text):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            return index
    return None


if __name__ == "__main__":
    data: str = Path("../input.txt").read_text()[0].strip()

    print(part_one(text=data))
    print(part_two(text=data))
