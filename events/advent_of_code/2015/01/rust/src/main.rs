//! # Advent of Code 2015 - Day 1

fn find_final_floor(text: &str) -> i32 {
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

fn find_when_santa_enters_basement(text: &str) -> i32 {
    let mut floor = 0;
    for (index, char) in text.chars().enumerate() {        
        if char == '(' {
            floor += 1;
        }
        if char == ')' {
            floor -= 1;
        }
        if floor == -1 {
            return (index + 1) as i32;
        }
    }
    panic!("Santa never enters the basement");
}

fn main() {
    let contents: &str = &std::fs::read_to_string("events/advent_of_code/2015/01/input.txt")
        .expect("Something went wrong reading the file");

    println!("{}", find_final_floor(contents));
    println!("{}", find_when_santa_enters_basement(contents));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = find_final_floor("(())");
        assert_eq!(result, 0);
        let result = find_final_floor("()()");
        assert_eq!(result, 0);
        let result = find_final_floor("(((");
        assert_eq!(result, 3);
        let result = find_final_floor("(()(()(");
        assert_eq!(result, 3);
        let result = find_final_floor("))(((((");
        assert_eq!(result, 3);
        let result = find_final_floor("())");
        assert_eq!(result, -1);
        let result = find_final_floor("))(");
        assert_eq!(result, -1);
        let result = find_final_floor(")))");
        assert_eq!(result, -3);
        let result = find_final_floor(")())())");
        assert_eq!(result, -3);


        let result = find_when_santa_enters_basement(")");
        assert_eq!(result, 1);
        let result = find_when_santa_enters_basement("()())");
        assert_eq!(result, 5);
    }
}
