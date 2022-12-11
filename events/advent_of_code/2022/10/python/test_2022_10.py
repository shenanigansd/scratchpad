from script_2022_10 import run_cycles, sum_cycles

EXAMPLE_INPUT = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -01
addx -8
addx 13
addx 4
noop
addx -01
addx 5
addx -01
addx 5
addx -01
addx 5
addx -01
addx 5
addx -01
addx -35
addx 01
addx 24
addx -19
addx 01
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 01
addx -3
addx 8
addx 01
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 01
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 01
noop
noop
addx 7
addx 01
noop
addx -13
addx 13
addx 7
noop
addx 01
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -01
addx 2
addx 01
noop
addx 17
addx -9
addx 01
addx 01
addx -3
addx 11
noop
noop
addx 01
noop
addx 01
noop
noop
addx -13
addx -19
addx 01
addx 3
addx 26
addx -30
addx 12
addx -01
addx 3
addx 01
noop
noop
noop
addx -9
addx 18
addx 01
addx 2
noop
noop
addx 9
noop
noop
noop
addx -01
addx 2
addx -37
addx 01
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 01
noop
addx 2
addx 01
noop
addx -10
noop
noop
addx 20
addx 01
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".strip()


def test_run_cycles() -> None:
    cycles = run_cycles(EXAMPLE_INPUT)

    assert cycles[20] * 20 == 420
    assert cycles[60] * 60 == 1140
    assert cycles[100] * 100 == 1800
    assert cycles[140] * 140 == 2940
    assert cycles[180] * 180 == 2880
    assert cycles[220] * 220 == 3960

    assert (
        sum_cycles(
            cycles,
            [
                20,
                60,
                100,
                140,
                180,
                220,
            ],
        )
        == 13140
    )
