import pytest
from find_distinct_sum import find_distinct_sum


@pytest.mark.parametrize(
    ("lst", "target", "result"),
    [
        ([1, 2, 3], 5, True),
        ([1, 2, 3], 10, False),
    ],
)
def test_find_distinct_sum(lst: list[int], target: int, result: bool) -> bool:  # noqa: FBT001 -- is testing boolean
    assert find_distinct_sum(lst, target=target) == result
