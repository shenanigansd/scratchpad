from pathlib import Path


def part_one(movements: list[tuple[str, int]]) -> int:
    directions = ["N", "E", "S", "W"]
    current_direction = "N"
    current_position = [0, 0]

    for directon, distance in movements:
        if directon == "R":
            current_direction = directions[(
                directions.index(current_direction) + 1) % 4]
        elif directon == "L":
            current_direction = directions[(
                directions.index(current_direction) - 1) % 4]

        match current_direction:
            case "N":
                current_position[1] += distance
            case "E":
                current_position[0] += distance
            case "S":
                current_position[1] -= distance
            case "W":
                current_position[0] -= distance

    return abs(current_position[0]) + abs(current_position[1])


def part_two(movements: list[tuple[str, int]]) -> int | None:
    directions = ["N", "E", "S", "W"]
    current_direction = "N"
    current_position = [0, 0]
    visited_positions = [(0,0)]

    for directon, distance in movements:
        if directon == "R":
            current_direction = directions[(
                directions.index(current_direction) + 1) % 4]
        elif directon == "L":
            current_direction = directions[(
                directions.index(current_direction) - 1) % 4]

        match current_direction:
            case "N":
                current_position[1] += distance
            case "E":
                current_position[0] += distance
            case "S":
                current_position[1] -= distance
            case "W":
                current_position[0] -= distance

        if tuple(current_position) in visited_positions:
            return abs(current_position[0]) + abs(current_position[1])
        
        visited_positions.append(tuple(current_position))
        print(visited_positions)


if __name__ == "__main__":
    raw_text: str = Path("input.txt").read_text()
    raw_items: list[str] = [item.strip() for item in raw_text.split(",")]
    items = [(item[0], int(item[1:])) for item in raw_items]
    print(len(items))

    print(part_one(movements=items))
    print(part_two(movements=items))
