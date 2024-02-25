import pytest
from aoc_2023_07 import JOKER_STRENGTH_ORDER, Hand, HandType, part1, part2

HANDS = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


@pytest.mark.parametrize(
    ("text", "hand"),
    [
        ("32T3K 765", Hand(cards="32T3K", type_=HandType.ONE_PAIR, bid=765)),
        ("T55J5 684", Hand(cards="T55J5", type_=HandType.THREE_OF_A_KIND, bid=684)),
        ("KK677 28", Hand(cards="KK677", type_=HandType.TWO_PAIR, bid=28)),
        ("KTJJT 220", Hand(cards="KTJJT", type_=HandType.TWO_PAIR, bid=220)),
        ("QQQJA 483", Hand(cards="QQQJA", type_=HandType.THREE_OF_A_KIND, bid=483)),
    ],
)
def test_can_parse_hand(text: str, hand: Hand) -> None:
    assert Hand.from_text(text) == hand


@pytest.mark.parametrize(
    ("text", "hand"),
    [
        (
            "32T3K 765",
            Hand(
                cards="32T3K",
                type_=HandType.ONE_PAIR,
                bid=765,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "T55J5 684",
            Hand(
                cards="T55J5",
                type_=HandType.FOUR_OF_A_KIND,
                bid=684,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "KK677 28",
            Hand(
                cards="KK677",
                type_=HandType.TWO_PAIR,
                bid=28,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "KTJJT 220",
            Hand(
                cards="KTJJT",
                type_=HandType.FOUR_OF_A_KIND,
                bid=220,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "QQQJA 483",
            Hand(
                cards="QQQJA",
                type_=HandType.FOUR_OF_A_KIND,
                bid=483,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "JJJJJ 99",
            Hand(
                cards="JJJJJ",
                type_=HandType.FIVE_OF_A_KIND,
                bid=99,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "JJAJJ 14",
            Hand(
                cards="JJAJJ",
                type_=HandType.FIVE_OF_A_KIND,
                bid=14,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "KKJJJ 28",
            Hand(
                cards="KKJJJ",
                type_=HandType.FIVE_OF_A_KIND,
                bid=28,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
        (
            "JJ558 33",
            Hand(
                cards="JJ558",
                type_=HandType.FOUR_OF_A_KIND,
                bid=33,
                strength_order=JOKER_STRENGTH_ORDER,
            ),
        ),
    ],
)
def test_can_parse_joker_hand(text: str, hand: Hand) -> None:
    assert Hand.from_text(text, using_jokers=True) == hand


def test_sorts_hands_correctly() -> None:
    hands = [Hand.from_text(line) for line in HANDS.strip().split("\n")]
    assert sorted(hands) == [
        Hand(cards="32T3K", type_=HandType.ONE_PAIR, bid=765),
        Hand(cards="KTJJT", type_=HandType.TWO_PAIR, bid=220),
        Hand(cards="KK677", type_=HandType.TWO_PAIR, bid=28),
        Hand(cards="T55J5", type_=HandType.THREE_OF_A_KIND, bid=684),
        Hand(cards="QQQJA", type_=HandType.THREE_OF_A_KIND, bid=483),
    ]


def test_sorts_joker_hands_correctly() -> None:
    hands = [Hand.from_text(line, using_jokers=True) for line in HANDS.strip().split("\n")]
    assert sorted(hands) == [
        Hand(
            cards="32T3K",
            type_=HandType.ONE_PAIR,
            bid=765,
            strength_order=JOKER_STRENGTH_ORDER,
        ),
        Hand(
            cards="KK677",
            type_=HandType.TWO_PAIR,
            bid=28,
            strength_order=JOKER_STRENGTH_ORDER,
        ),
        Hand(
            cards="T55J5",
            type_=HandType.FOUR_OF_A_KIND,
            bid=684,
            strength_order=JOKER_STRENGTH_ORDER,
        ),
        Hand(
            cards="QQQJA",
            type_=HandType.FOUR_OF_A_KIND,
            bid=483,
            strength_order=JOKER_STRENGTH_ORDER,
        ),
        Hand(
            cards="KTJJT",
            type_=HandType.FOUR_OF_A_KIND,
            bid=220,
            strength_order=JOKER_STRENGTH_ORDER,
        ),
    ]


def test_part1_matches_sample_answer() -> None:
    hands = [Hand.from_text(line) for line in HANDS.strip().split("\n")]
    assert part1(hands) == 6440


def test_part2_matches_sample_answer() -> None:
    hands = [Hand.from_text(line, using_jokers=True) for line in HANDS.strip().split("\n")]
    assert part2(hands) == 5905
