from script_2021_03 import get_rates

EXAMPLE_INPUT = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()


def test_get_rates() -> None:
    assert get_rates(EXAMPLE_INPUT.splitlines()) == ("10110", "01001")
