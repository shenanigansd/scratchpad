def part_one(text: str) -> int:
    return sum(1 if char == "(" else -1 for char in text)


def part_two(text: str) -> int:
    index = 0
    floor = 0
    for char in text:
        index += 1
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            return index


if __name__ == "__main__":
    data: str = open("../../../input.txt").readlines()[0].strip()

    print(part_one(text=data))
    print(part_two(text=data))
