from pathlib import Path


def parse_input(text: str) -> list[list[int]]:
    return [list(map(int, line)) for line in text.split("\n") if line]


def part1(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        biggest = max(bank[:-1])
        next_biggest = max(bank[bank.index(biggest) + 1 :])
        total += int(f"{biggest}{next_biggest}")
    return total


def part2(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        while len(bank) > 12:
            bank.remove(min(bank))
        total += int("".join(map(str, bank)))
    return total


if __name__ == "__main__":
    text = Path("../input.txt").read_text(encoding="locale")
    values = parse_input(text)
    print(part1(values))
    print(part2(values))
