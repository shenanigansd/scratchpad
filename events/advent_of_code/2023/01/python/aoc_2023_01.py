import re
from pathlib import Path


def find_numbers_and_number_words_in_text(text: str) -> list[int]:
    values = []
    regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    for group in re.findall(regex, text):
        match group:
            case "one":
                values.append(1)
            case "two":
                values.append(2)
            case "three":
                values.append(3)
            case "four":
                values.append(4)
            case "five":
                values.append(5)
            case "six":
                values.append(6)
            case "seven":
                values.append(7)
            case "eight":
                values.append(8)
            case "nine":
                values.append(9)
            case _:
                values.append(int(group))
    return values


def find_numbers_in_text(text: str) -> list[int]:
    return [int(item) for item in re.findall(r"\d", text)]


def find_first_and_last_number_in_text(
    text: str,
    text_contains_spelled_words: bool = False,  # noqa: FBT001,FBT002
) -> tuple[int, int]:
    numbers = find_numbers_and_number_words_in_text(text) if text_contains_spelled_words else find_numbers_in_text(text)
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    return numbers[0], numbers[-1]


def part1(rows: list[str]) -> int:
    return sum(int(str("".join(str(item) for item in find_first_and_last_number_in_text(row)))) for row in rows)


def part2(rows: list[str]) -> int:
    return sum(
        int(
            str(
                "".join(
                    str(item)
                    for item in find_first_and_last_number_in_text(
                        row,
                        text_contains_spelled_words=True,
                    )
                ),
            ),
        )
        for row in rows
    )


if __name__ == "__main__":
    rows = Path("../input.txt").read_text(encoding="locale").split("\n")
    print(part1(rows))
    print(part2(rows))
