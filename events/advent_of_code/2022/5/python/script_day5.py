from dataclasses import dataclass

from darbia.utils.iterables import chunks


@dataclass
class Warehouse:
    stacks: dict[int, list[str]]

    @classmethod
    def build_from(cls, text: str) -> "Warehouse":
        header, *lines = list(reversed(text.splitlines()))
        lines.remove("")
        stack_count = len(header.split())
        warehouse = Warehouse({index: [] for index in range(1, stack_count + 1)})
        for line in lines:
            stack = 1
            for chunk in chunks(line, 4):
                if chunk[0] == "[":
                    warehouse.stacks[stack].append(chunk[1])
                stack += 1
        return warehouse


def part_one(values: list[tuple[set[int], set[int]]]) -> int:
    total = 0
    return total


def part_two(values: list[tuple[set[int], set[int]]]) -> int:
    total = 0
    return total


if __name__ == "__main__":
    pass
    # data = [
    #     (set(_range_parser(item.split(",")[0])), set(_range_parser(item.split(",")[1])))
    #     for item in Path("../../../input.txt").read_text().strip().split("\n")
    # ]
    # print(part_one(values=data))
    # print(part_two(values=data))
