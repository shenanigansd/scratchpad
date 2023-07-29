import pytest
from script_2016_01 import part_one, part_two


@pytest.mark.parametrize(
    "movements,distance",
    [
        ([("R", 2), ("L", 3)], 5),
        ([("R", 2), ("R", 2), ("R", 2)], 2),
        ([("R", 5), ("L", 5), ("R", 5), ("R", 3)], 12),
    ],
)
def test_part_one(movements: list[tuple[str, int]], distance: int) -> None:
    assert part_one(movements) == distance


@pytest.mark.parametrize(
    "movements,distance",
    [
        ([("R", 8), ("R", 4), ("R", 4), ("R", 8)], 4),
    ],
)
def test_part_two(movements: list[tuple[str, int]], distance: int) -> None:
    assert part_two(movements) == distance
