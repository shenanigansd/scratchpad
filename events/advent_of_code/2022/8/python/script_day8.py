import math
from pathlib import Path


def get_visible_trees(grid: list[list[int]]) -> int:
    visible_trees = 0
    visible_trees += len(grid) * 2
    visible_trees += len(grid[0]) * 2
    visible_trees -= 4
    for row_index, row in enumerate(grid[1:-1]):
        for tree_index, tree in enumerate(row[1:-1]):
            visible_left = all(left_tree < tree for left_tree in row[: tree_index + 1])

            visible_right = all(right_tree < tree for right_tree in row[tree_index + 2 :])

            trees_above = [row_[tree_index + 1] for row_ in grid[: row_index + 1]]
            visible_up = all(up_tree < tree for up_tree in trees_above)

            trees_below = [row_[tree_index + 1] for row_ in grid[row_index + 2 :]]
            visible_down = all(down_tree < tree for down_tree in trees_below)

            if any(
                [
                    visible_left,
                    visible_right,
                    visible_up,
                    visible_down,
                ]
            ):
                visible_trees += 1

    return visible_trees


def get_scenic_scores(grid: list[list[int]]) -> int:
    scenic_scores = []
    for row_index, row in enumerate(grid):
        for tree_index, tree in enumerate(row):
            trees_left = list(left_tree for left_tree in row[:tree_index])
            trees_right = list(right_tree for right_tree in row[tree_index + 1 :])
            trees_above = [row_[tree_index] for row_ in grid[:row_index]]
            trees_below = [row_[tree_index] for row_ in grid[row_index + 1 :]]

            direction_scores = []
            for tree_list in [
                reversed(trees_left),
                trees_right,
                reversed(trees_above),
                trees_below,
            ]:
                direction_score = 0
                for tree_ in tree_list:
                    if tree_ < tree:
                        direction_score += 1
                    else:
                        direction_score += 1
                        break
                direction_scores.append(direction_score)

            scenic_scores.append(math.prod(direction_scores))
            direction_scores.clear()

    return max(scenic_scores)


def part_one(grid: list[list[int]]) -> int:
    return get_visible_trees(grid)


def part_two(grid: list[list[int]]) -> int:
    return get_scenic_scores(grid)


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    grid_ = [[int(char) for char in line] for line in data.splitlines()]
    print(part_one(grid_))
    print(part_two(grid_))
