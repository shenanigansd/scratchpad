use itertools::Itertools;

fn find_unique_window(text: &str, length: usize) -> usize {
    let chars = String::from(text).chars().collect::<Vec<char>>();
    let windows = chars.windows(length);

    for (x, window) in windows.enumerate() {
        if window.iter().unique().count() == length {
            return length + x;
        }
    }
    panic!("did not find")
}

fn part_one(text: &str) -> usize {
    find_unique_window(text, 4)
}

fn part_two(text: &str) -> usize {
    find_unique_window(text, 14)
}

fn main() {
    let contents: &str =
        &std::fs::read_to_string("../input.txt").expect("Something went wrong reading the file");

    println!("{}", part_one(contents));
    println!("{}", part_two(contents));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = find_unique_window("bvwbjplbgvbhsrlpgdmjqwftvncz", 4);
        assert_eq!(result, 5);
        let result = find_unique_window("nppdvjthqldpwncqszvftbrmjlhg", 4);
        assert_eq!(result, 6);
        let result = find_unique_window("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4);
        assert_eq!(result, 10);
        let result = find_unique_window("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4);
        assert_eq!(result, 11);

        let result = find_unique_window("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14);
        assert_eq!(result, 19);
        let result = find_unique_window("bvwbjplbgvbhsrlpgdmjqwftvncz", 14);
        assert_eq!(result, 23);
        let result = find_unique_window("nppdvjthqldpwncqszvftbrmjlhg", 14);
        assert_eq!(result, 23);
        let result = find_unique_window("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14);
        assert_eq!(result, 29);
        let result = find_unique_window("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14);
        assert_eq!(result, 26);
    }
}
