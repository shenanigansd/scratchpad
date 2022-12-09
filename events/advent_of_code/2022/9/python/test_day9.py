from script_day9 import Movement, Rope, part_two

EXAMPLE_INPUT = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
    """.strip()


def test_rope() -> None:
    movements = [Movement.build_from(line) for line in EXAMPLE_INPUT.splitlines()]
    rope = Rope(head=(0, 0), tail=(0, 0))
    for movement in movements:
        rope.move(movement)
    assert len(set(rope.tail_visited)) == 13


def test_part_two() -> None:
    movements = [Movement.build_from(line) for line in EXAMPLE_INPUT.splitlines()]
    assert part_two(movements) == 36
