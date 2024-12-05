import pytest
from aoc_2024_01 import Report


@pytest.mark.parametrize(
    ("values", "is_safe"),
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_report_is_safe(values: list[int], is_safe: bool) -> None:  # noqa: FBT001
    assert Report(values).is_safe() == is_safe


@pytest.mark.parametrize(
    ("values", "is_safe"),
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_report_is_safe_wth_dampener(values: list[int], is_safe: bool) -> None:  # noqa: FBT001
    assert Report(values).is_safe(dampener_enabled=True) == is_safe
