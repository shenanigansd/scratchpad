use rayon::prelude::*;
use std::fs;
use std::str::FromStr;

fn parse_map(text: &str) -> Vec<(i64, i64, i64)> {
    text.split('\n')
        .skip(1)
        .map(|line| {
            let parts = line.split(' ').collect::<Vec<&str>>();
            (
                parts[0].parse().unwrap(),
                parts[1].parse().unwrap(),
                parts[2].parse().unwrap(),
            )
        })
        .collect()
}

fn find_map_position(value: i64, map: &[(i64, i64, i64)]) -> i64 {
    for &(destination_start, source_start, range) in map {
        if source_start <= value && value < source_start + range {
            return destination_start + value - source_start;
        }
    }
    value
}

#[derive(Debug)]
struct Almanac {
    seeds: Vec<i64>,
    maps: Vec<Vec<(i64, i64, i64)>>,
}

#[derive(Debug, PartialEq, Eq)]
struct ParseAlmanacError;

impl FromStr for Almanac {
    type Err = ParseAlmanacError;

    fn from_str(text: &str) -> Result<Self, Self::Err> {
        let parts = text.trim().split("\n\n").collect::<Vec<&str>>();
        let seeds_text: &str = parts[0].split(':').collect::<Vec<&str>>()[1].trim();
        let seeds: Vec<i64> = seeds_text
            .split(' ')
            .map(|seed| seed.parse().unwrap())
            .collect();

        Ok(Almanac {
            seeds,
            maps: (1..8).map(|i| parse_map(parts[i])).collect(),
        })
    }
}

impl Almanac {
    fn seed_location(&self, seed: i64) -> i64 {
        self.maps
            .iter()
            .fold(seed, |acc, map| find_map_position(acc, map))
    }

    fn smallest_seed_location(&self) -> i64 {
        self.seeds
            .iter()
            .map(|&seed| self.seed_location(seed))
            .min()
            .unwrap()
    }

    fn smallest_seed_range_location(&self) -> i64 {
        self.seeds
            .chunks(2)
            .filter_map(|pair| {
                (pair[0]..pair[0] + pair[1])
                    .into_par_iter()
                    .map(|seed| self.seed_location(seed))
                    .min()
            })
            .min()
            .unwrap()
    }
}

fn main() {
    let input = fs::read_to_string("events/advent_of_code/2023/05/input.txt")
        .expect("Should have been able to read the file");
    let almanac = Almanac::from_str(&input).unwrap();
    println!("{}", almanac.smallest_seed_location());
    println!("{}", almanac.smallest_seed_range_location());
}
