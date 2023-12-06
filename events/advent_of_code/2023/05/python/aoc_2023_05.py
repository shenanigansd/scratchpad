from dataclasses import dataclass
from pathlib import Path
from darbia.utils.iterables import chunks

@dataclass(frozen=True)
class Almanac:
    seeds: list[int]

    seed_to_soil_map: list[tuple[int, int, int]]
    soil_to_fertilizer_map: list[tuple[int, int, int]]
    fertilizer_to_water_map: list[tuple[int, int, int]]
    water_to_light_map: list[tuple[int, int, int]]
    light_to_temperature_map: list[tuple[int, int, int]]
    temperature_to_humidity_map: list[tuple[int, int, int]]
    humidity_to_location_map: list[tuple[int, int, int]]

    @classmethod
    def from_text(cls, text: str) -> "Almanac":
        lines = text.split("\n\n")
        seeds = [int(s) for s in lines[0].split(":")[1].split()]
        seed_to_soil_map = [tuple(int(s) for s in line.split()) for line in lines[1].split("\n")[1:]]
        soil_to_fertilizer_map = [tuple(int(s) for s in line.split()) for line in lines[2].split("\n")[1:]]
        fertilizer_to_water_map = [tuple(int(s) for s in line.split()) for line in lines[3].split("\n")[1:]]
        water_to_light_map = [tuple(int(s) for s in line.split()) for line in lines[4].split("\n")[1:]]
        light_to_temperature_map = [tuple(int(s) for s in line.split()) for line in lines[5].split("\n")[1:]]
        temperature_to_humidity_map = [tuple(int(s) for s in line.split()) for line in lines[6].split("\n")[1:]]
        humidity_to_location_map = [tuple(int(s) for s in line.split()) for line in lines[7].split("\n")[1:] if line]
        return cls(
            seeds,
            seed_to_soil_map,
            soil_to_fertilizer_map,
            fertilizer_to_water_map,
            water_to_light_map,
            light_to_temperature_map,
            temperature_to_humidity_map,
            humidity_to_location_map,
        )

    def smallest_seed_location(self) -> int:
        min_location = float("inf")
        for seed in self.seeds:
            location = seed
            maps = [
                self.seed_to_soil_map,
                self.soil_to_fertilizer_map,
                self.fertilizer_to_water_map,
                self.water_to_light_map,
                self.light_to_temperature_map,
                self.temperature_to_humidity_map,
                self.humidity_to_location_map,
            ]
            for map_ in maps:
                location = find_map_position(location, map_)
            if location < min_location:
                min_location = location
        return min_location

    def smallest_seed_range_location(self) -> int:
        min_location = float("inf")
        for (start_seed, range_) in chunks(self.seeds, 2):
            for seed in range(start_seed, start_seed + range_):
                location = seed
                maps = [
                    self.seed_to_soil_map,
                    self.soil_to_fertilizer_map,
                    self.fertilizer_to_water_map,
                    self.water_to_light_map,
                    self.light_to_temperature_map,
                    self.temperature_to_humidity_map,
                    self.humidity_to_location_map,
                ]
                for map_ in maps:
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
