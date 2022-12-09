import pytest

from script_day9 import Movement, run

EXAMPLE_INPUT_PART_ONE = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
    """.strip()

EXAMPLE_INPUT_PART_TWO = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip()


@pytest.mark.parametrize(
    "knots_quantity,data,result",
    [
        (1, EXAMPLE_INPUT_PART_ONE, 13),
        (10, EXAMPLE_INPUT_PART_TWO, 36),
    ],
)
def test_knots(knots_quantity: int, data: str, result: int) -> None:
    movements = [Movement.build_from(line) for line in data.splitlines()]
    assert run(knots_quantity, movements) == result
