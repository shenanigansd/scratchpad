use std::fs;

fn parse_map(text: &str) -> Vec<(i64, i64, i64)> {
    text.split("\n")
        .skip(1)
        .map(|line| {
            let parts = line.split(" ").collect::<Vec<&str>>();
            (
                parts[0].parse().unwrap(),
                parts[1].parse().unwrap(),
                parts[2].parse().unwrap(),
            )
        })
        .collect()
}

fn find_map_position(value: i64, map: Vec<(i64, i64, i64)>) -> i64 {
    for (destination_start, source_start, range) in map {
        if source_start <= value && value < source_start + range {
            return destination_start + value - source_start;
        }
    }
    value
}

#[derive(Debug)]
struct Almanac {
    seeds: Vec<i64>,

    seed_to_soil_map: Vec<(i64, i64, i64)>,
    soil_to_fertilizer_map: Vec<(i64, i64, i64)>,
    fertilizer_to_water_map: Vec<(i64, i64, i64)>,
    water_to_light_map: Vec<(i64, i64, i64)>,
    light_to_temperature_map: Vec<(i64, i64, i64)>,
    temperature_to_humidity_map: Vec<(i64, i64, i64)>,
    humidity_to_location_map: Vec<(i64, i64, i64)>,
}

fn almanac_from_text(text: &str) -> Almanac {
    let parts = text.trim().split("\n\n").collect::<Vec<&str>>();
    let seeds_text: &str = parts[0].split(":").collect::<Vec<&str>>()[1].trim();
    let seeds: Vec<i64> = seeds_text
        .split(" ")
        .map(|seed| seed.parse().unwrap())
        .collect();

    let seed_to_soil_map: Vec<(i64, i64, i64)> = parse_map(parts[1]);
    let soil_to_fertilizer_map: Vec<(i64, i64, i64)> = parse_map(parts[2]);
    let fertilizer_to_water_map: Vec<(i64, i64, i64)> = parse_map(parts[3]);
    let water_to_light_map: Vec<(i64, i64, i64)> = parse_map(parts[4]);
    let light_to_temperature_map: Vec<(i64, i64, i64)> = parse_map(parts[5]);
    let temperature_to_humidity_map: Vec<(i64, i64, i64)> = parse_map(parts[6]);
    let humidity_to_location_map: Vec<(i64, i64, i64)> = parse_map(parts[7]);

    Almanac {
        seeds,
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
    }
}

impl Almanac {
    fn smallest_seed_location(&self) -> i64 {
        let mut smallest_seed_location = i64::MAX;
        for seed in &self.seeds {
            let seed_location = seed;
            let seed_location = find_map_position(*seed_location, self.seed_to_soil_map.clone());
            let seed_location =
                find_map_position(seed_location, self.soil_to_fertilizer_map.clone());
            let seed_location =
                find_map_position(seed_location, self.fertilizer_to_water_map.clone());
            let seed_location = find_map_position(seed_location, self.water_to_light_map.clone());
            let seed_location =
                find_map_position(seed_location, self.light_to_temperature_map.clone());
            let seed_location =
                find_map_position(seed_location, self.temperature_to_humidity_map.clone());
            let seed_location =
                find_map_position(seed_location, self.humidity_to_location_map.clone());

            if seed_location < smallest_seed_location {
                smallest_seed_location = seed_location;
            }
        }
        smallest_seed_location
    }
    fn smallest_seed_range_location(&self) -> i64 {
        let mut smallest_seed_location = i64::MAX;
        for pair in self.seeds.chunks(2){
        for seed in  pair[0]..pair[0]+pair[1] {
            let seed_location = seed;
            let seed_location = find_map_position(seed_location, self.seed_to_soil_map.clone());
            let seed_location =
                find_map_position(seed_location, self.soil_to_fertilizer_map.clone());
            let seed_location =
                find_map_position(seed_location, self.fertilizer_to_water_map.clone());
            let seed_location = find_map_position(seed_location, self.water_to_light_map.clone());
            let seed_location =
                find_map_position(seed_location, self.light_to_temperature_map.clone());
            let seed_location =
                find_map_position(seed_location, self.temperature_to_humidity_map.clone());
            let seed_location =
                find_map_position(seed_location, self.humidity_to_location_map.clone());

            if seed_location < smallest_seed_location {
                smallest_seed_location = seed_location;
            }
        }}
        smallest_seed_location
    }
}

fn main() {
    let input = fs::read_to_string("events/advent_of_code/2023/05/input.txt")
        .expect("Should have been able to read the file");
    let almanac = almanac_from_text(&input);
    println!("{:?}", almanac.smallest_seed_location());
    println!("{:?}", almanac.smallest_seed_range_location());
}
