from script_day5 import Warehouse


def test_parse_warehouse():
    text = """
[T]     [Q]             [S]       
[R]     [M]             [L] [V] [G]
[D] [V] [V]             [Q] [N] [C]
[H] [T] [S] [C]         [V] [D] [Z]
[Q] [J] [D] [M]     [Z] [C] [M] [F]
[N] [B] [H] [N] [B] [W] [N] [J] [M]
[P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
[B] [W] [N] [P] [D] [V] [G] [L] [T]
 1   2   3   4   5   6   7   8   9
"""
    test_warehouse = Warehouse(
        stacks={
            1: ["B", "P", "N", "Q", "H", "D", "R", "T"],
            2: ["W", "G", "B", "J", "T", "V"],
            3: ["N", "R", "H", "D", "S", "V", "M", "Q"],
            4: ["P", "Z", "N", "M", "C"],
            5: ["D", "Z", "B"],
            6: ["V", "C", "W", "Z"],
            7: ["G", "Z", "N", "C", "V", "Q", "L", "S"],
            8: ["L", "G", "J", "M", "D", "N", "V"],
            9: ["T", "P", "M", "F", "Z", "C", "G"],
        }
    )

    assert Warehouse.build_from(text) == test_warehouse
