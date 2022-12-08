from script_day8 import get_scenic_scores, get_visible_trees

EXAMPLE_INPUT = """
    30373
    25512
    65332
    33549
    35390
    """.strip()


def test_get_visible_trees() -> None:
    grid = [[int(char) for char in line.strip()] for line in EXAMPLE_INPUT.splitlines()]
    assert get_visible_trees(grid) == 21


def test_get_scenic_scores() -> None:
    grid = [[int(char) for char in line.strip()] for line in EXAMPLE_INPUT.splitlines()]
    assert get_scenic_scores(grid) == 8
