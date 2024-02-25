from dataclasses import dataclass
from itertools import batched
from pathlib import Path


@dataclass(frozen=True)
class Almanac:
    seeds: list[int]
    maps: list[list[tuple[int, int, int]]]

    @classmethod
    def from_text(cls, text: str) -> "Almanac":
        lines = text.split("\n\n")
        seeds = [int(s) for s in lines[0].split(":")[1].split()]

        maps = []
        for lines_group in lines[1:]:
            titleless_lines = lines_group.split("\n")
            titleless_lines.pop(0)
            maps.append([tuple(int(s) for s in line.split()) for line in titleless_lines if line])

        return cls(seeds, maps)

    def smallest_seed_location(self) -> int:
        min_location = float("inf")
        for seed in self.seeds:
            location = seed
            for map_ in self.maps:
                location = find_map_position(location, map_)
            if location < min_location:
                min_location = location
        return min_location

    def smallest_seed_range_location(self) -> int:
        min_location = float("inf")
        for start_seed, range_ in batched(self.seeds, 2):
            for seed in range(start_seed, start_seed + range_):
                location = seed
                for map_ in self.maps:
                    location = find_map_position(location, map_)
                if location < min_location:
                    min_location = location
        return min_location


def find_map_position(value: int, map_: list[tuple[int, int, int]]) -> int:
    for destination_start, source_start, range_ in map_:
        if source_start <= value < source_start + range_:
            return destination_start + value - source_start
    return value


def part1(almanac: Almanac) -> int:
    return almanac.smallest_seed_location()


def part2(almanac: Almanac) -> int:
    return almanac.smallest_seed_range_location()


if __name__ == "__main__":
    text = Path("../input.txt").read_text()
    almanac = Almanac.from_text(text)
    print(part1(almanac))
    print(part2(almanac))
