from aoc_2023_05 import Almanac

RAW_INPUT = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

TEST_ALMANAC = Almanac(
    seeds=[79, 14, 55, 13],
    seed_to_soil_map=[(50, 98, 2), (52, 50, 48)],
    soil_to_fertilizer_map=[(0, 15, 37), (37, 52, 2), (39, 0, 15)],
    fertilizer_to_water_map=[(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)],
    water_to_light_map=[(88, 18, 7), (18, 25, 70)],
    light_to_temperature_map=[(45, 77, 23), (81, 45, 19), (68, 64, 13)],
    temperature_to_humidity_map=[(0, 69, 1), (1, 0, 69)],
    humidity_to_location_map=[(60, 56, 37), (56, 93, 4)],
)


def test_can_parse_almanac() -> None:
    assert Almanac.from_text(RAW_INPUT) == TEST_ALMANAC

def test_can_find_smallest_location() -> None:
    assert TEST_ALMANAC.smallest_seed_location() == 35

def test_can_find_smallest_range_location() -> None:
    assert TEST_ALMANAC.smallest_seed_range_location() == 46
