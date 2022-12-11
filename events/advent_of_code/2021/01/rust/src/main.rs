use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}

fn count_larger_nexts(numbers: &[u16]) -> i32 {
    let mut count = 0;
    for (position, current_number) in numbers.iter().skip(1).enumerate() {
        let last_number = &numbers[position];
        if current_number > last_number {
            count += 1;
        }
    }
    count
}

fn part_one(numbers: &[u16]) -> i32 {
    count_larger_nexts(numbers)
}

fn part_two(numbers: &[u16]) -> i32 {
    let mut sums: Vec<u16> = Vec::new();
    for (position, current_number) in numbers.iter().skip(2).enumerate() {
        sums.push(current_number + numbers[position] + numbers[position + 1]);
    }

    count_larger_nexts(&sums)
}

fn main() {
    let lines =
        lines_from_file("events/advent_of_code/2021/01/input.txt").expect("Could not load lines");
    let numbers: Vec<u16> = lines.iter().map(|num| num.parse().unwrap()).collect();

    println!("{}", part_one(&numbers));
    println!("{}", part_two(&numbers));
}
