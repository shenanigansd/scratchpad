from hypothesis import given
from hypothesis import strategies as st


@given(st.integers(), st.integers())
def test_ints_are_commutative(x: int, y: int) -> None:
    assert x + y == y + x


@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x: int, y: int) -> None:
    assert (x + y) - y == x


@given(st.lists(st.integers()))
def test_reversing_twice_gives_same_list(xs: list[int]) -> None:
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys


@given(st.tuples(st.booleans(), st.text()))
def test_look_tuples_work_too(t: tuple[bool, str]) -> None:
    # A tuple is generated as the one you provided, with the corresponding
    # types in those positions.
    assert len(t) == 2  # noqa: PLR2004 -- Value is not reused.
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)
