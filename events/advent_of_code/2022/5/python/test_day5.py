from script_day5 import Movement, Warehouse


def test_parse_warehouse():
    text = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""
    test_warehouse = Warehouse(
        stacks={
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        }
    )

    assert Warehouse.build_from(text) == test_warehouse


def test_warehouse_move_single():
    test_warehouse = Warehouse(
        stacks={
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        }
    )

    movement1 = Movement(1, 2, 1)
    warehouse_after_movement1 = Warehouse(
        stacks={
            1: ["Z", "N", "D"],
            2: ["M", "C"],
            3: ["P"],
        }
    )
    test_warehouse.move_single(movement1)
    assert test_warehouse == warehouse_after_movement1

    movement2 = Movement(3, 1, 3)
    warehouse_after_movement2 = Warehouse(
        stacks={
            1: [],
            2: ["M", "C"],
            3: ["P", "D", "N", "Z"],
        }
    )
    test_warehouse.move_single(movement2)
    assert test_warehouse == warehouse_after_movement2

    movement3 = Movement(2, 2, 1)
    warehouse_after_movement3 = Warehouse(
        stacks={
            1: ["C", "M"],
            2: [],
            3: ["P", "D", "N", "Z"],
        }
    )
    test_warehouse.move_single(movement3)
    assert test_warehouse == warehouse_after_movement3

    movement4 = Movement(1, 1, 2)
    warehouse_after_movement4 = Warehouse(
        stacks={
            1: ["C"],
            2: ["M"],
            3: ["P", "D", "N", "Z"],
        }
    )
    test_warehouse.move_single(movement4)
    assert test_warehouse == warehouse_after_movement4

    assert test_warehouse.tops() == "CMZ"


def test_warehouse_move_bulk():
    test_warehouse = Warehouse(
        stacks={
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        }
    )

    movement1 = Movement(1, 2, 1)
    warehouse_after_movement1 = Warehouse(
        stacks={
            1: ["Z", "N", "D"],
            2: ["M", "C"],
            3: ["P"],
        }
    )
    test_warehouse.move_bulk(movement1)
    assert test_warehouse == warehouse_after_movement1

    movement2 = Movement(3, 1, 3)
    warehouse_after_movement2 = Warehouse(
        stacks={
            1: [],
            2: ["M", "C"],
            3: ["P", "Z", "N", "D"],
        }
    )
    test_warehouse.move_bulk(movement2)
    assert test_warehouse == warehouse_after_movement2

    movement3 = Movement(2, 2, 1)
    warehouse_after_movement3 = Warehouse(
        stacks={
            1: ["M", "C"],
            2: [],
            3: ["P", "Z", "N", "D"],
        }
    )
    test_warehouse.move_bulk(movement3)
    assert test_warehouse == warehouse_after_movement3

    movement4 = Movement(1, 1, 2)
    warehouse_after_movement4 = Warehouse(
        stacks={
            1: ["M"],
            2: ["C"],
            3: ["P", "Z", "N", "D"],
        }
    )
    test_warehouse.move_bulk(movement4)
    assert test_warehouse == warehouse_after_movement4

    assert test_warehouse.tops() == "MCD"
