from pathlib import Path

from darbia.utils.iterables import chunks


def run_cycles(text: str) -> dict[int, int]:
    cycles = {}
    lines = text.splitlines()
    cycle = 1
    x = 1
    for line in lines:
        match line.split():
            case ["noop"]:
                cycle += 1
                cycles[cycle] = x
            case ["addx", number]:
                cycle += 1
                cycles[cycle] = x
                cycle += 1
                x += int(number)
                cycles[cycle] = x
    return cycles


def sum_cycles(cycles: dict[int, int], wanted: list[int]) -> int:
    return sum(cycles[want] * want for want in wanted)


def part_one(text: str) -> int:
    return sum_cycles(
        run_cycles(text),
        [
            20,
            60,
            100,
            140,
            180,
            220,
        ],
    )


def part_two(text: str) -> str:
    pixels = []
    cycles = run_cycles(text)
    for cycle, x in cycles.items():
        pixels.append("#" if x - 1 <= (cycle - 1) % 40 <= x + 1 else " ")
    return "\n".join("".join(row) for row in chunks(pixels, 40))


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    print(part_one(data))
    print(part_two(data))
