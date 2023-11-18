from dataclasses import dataclass


@dataclass
class Box:
    length: int
    width: int
    height: int

    def sides_by_length(self) -> list[int]:
        return sorted([self.length, self.width, self.height])


def part_one(boxes: list[Box]) -> int:
    total = 0
    for box in boxes:
        sides = (
            box.length * box.width,
            box.width * box.height,
            box.height * box.length,
        )
        smallest_side = min(sides)
        total += sum(sides) * 2 + smallest_side
    return total


def part_two(boxes: list[Box]) -> int:
    total = 0
    for box in boxes:
        total += sum(box.sides_by_length()[0:2]) * 2 + box.length * box.width * box.height
    return total


if __name__ == "__main__":
    lines: list[str] = open("../input.txt").readlines()
    boxes_: list[Box] = [Box(*map(int, line.split("x"))) for line in lines]

    print(part_one(boxes=boxes_))
    print(part_two(boxes=boxes_))
