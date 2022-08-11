fn part_one(text: &str) -> i32 {
    let mut floor = 0;
    for char in text.chars() {
        if char == '(' {
            floor += 1;
        }
        if char == ')' {
            floor -= 1;
        }
    }
    floor
}

fn part_two(text: &str) -> i32 {
    let mut index = 0;
    let mut floor = 0;
    for char in text.chars() {
        index += 1;
        if char == '(' {
            floor += 1;
        }
        if char == ')' {
            floor -= 1;
        }
        if floor == -1 {
            return index;
        }
    }
    index
}

fn main() {
    let contents: &str =
        &std::fs::read_to_string("../../input.txt").expect("Something went wrong reading the file");

    println!("{}", part_one(&contents));
    println!("{}", part_two(&contents));
}
