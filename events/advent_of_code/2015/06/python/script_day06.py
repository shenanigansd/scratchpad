from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Event:
    action: str
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    @classmethod
    def from_str(cls, text):
        text = text.replace("turn ", "")
        texts = text.split(" ")

        action = texts[0]
        start_x, start_y = map(int, texts[1].split(","))
        end_x, end_y = map(int, texts[3].split(","))

        return cls(action, start_x, start_y, end_x, end_y)


def part_one(events: list[Event]) -> int:
    lit_lights = set()
    for event in events:
        for x in range(event.start_x, event.end_x + 1):
            for y in range(event.start_y, event.end_y + 1):
                match event.action:
                    case "on":
                        lit_lights.add((x, y))
                    case "off":
                        if (x, y) in lit_lights:
                            lit_lights.remove((x, y))
                    case "toggle":
                        if (x, y) in lit_lights:
                            lit_lights.remove((x, y))
                        else:
                            lit_lights.add((x, y))

    return len(lit_lights)


def part_two(events: list[Event]) -> int:
    brightnesses: dict[tuple[int, int], int] = defaultdict(int)
    for event in events:
        for x in range(event.start_x, event.end_x + 1):
            for y in range(event.start_y, event.end_y + 1):
                match event.action:
                    case "on":
                        brightnesses[(x, y)] += 1
                    case "off":
                        brightnesses[(x, y)] -= 1
                        if brightnesses[(x, y)] < 0:
                            brightnesses[(x, y)] = 0
                    case "toggle":
                        brightnesses[(x, y)] += 2

    return sum(brightnesses.values())


if __name__ == "__main__":
    data: list[str] = Path("../../../input.txt").read_text().strip().split("\n")
    events_: list[Event] = [Event.from_str(item) for item in data]
    print(events_[0])

    print(part_one(events=events_))
    print(part_two(events=events_))
