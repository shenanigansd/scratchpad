from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path
from typing import Self

STRENGTH_ORDER = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
JOKER_STRENGTH_ORDER = ("J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A")


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass(frozen=True)
class Hand:
    cards: str
    type_: HandType
    bid: int
    strength_order: tuple[str] = STRENGTH_ORDER

    @classmethod
    def from_text(cls: type[Self], text: str, using_jokers: bool = False) -> Self:  # noqa: FBT001,FBT002
        cards, bid = text.split()
        bid = int(bid)
        counter = dict(Counter(cards))
        if using_jokers:
            j_s = counter.pop("J", 0)
            if j_s == 5:
                counter = {"J": 5}
            else:
                most_populus_card = max(counter, key=counter.get)
                counter[most_populus_card] += j_s
        card_counts = sorted(counter.values(), reverse=True)
        hand_type = None
        match card_counts:
            case [5]:
                hand_type = HandType.FIVE_OF_A_KIND
            case [4, 1]:
                hand_type = HandType.FOUR_OF_A_KIND
            case [3, 2]:
                hand_type = HandType.FULL_HOUSE
            case [3, 1, 1]:
                hand_type = HandType.THREE_OF_A_KIND
            case [2, 2, 1]:
                hand_type = HandType.TWO_PAIR
            case [2, 1, 1, 1]:
                hand_type = HandType.ONE_PAIR
            case [1, 1, 1, 1, 1]:
                hand_type = HandType.HIGH_CARD
            case _:
                msg = f"Invalid hand: {text}"
                raise ValueError(msg)
        strength_order = JOKER_STRENGTH_ORDER if using_jokers else STRENGTH_ORDER
        return cls(cards=cards, bid=bid, type_=hand_type, strength_order=strength_order)

    def __lt__(self: Self, other: Self) -> bool:
        if self.type_ < other.type_:
            return True
        if self.type_ > other.type_:
            return False
        for self_card, other_card in zip(self.cards, other.cards, strict=True):
            if self.strength_order.index(self_card) < self.strength_order.index(
                other_card,
            ):
                return True
            if self.strength_order.index(self_card) > self.strength_order.index(
                other_card,
            ):
                return False
        msg = "Hands are equal"
        raise ValueError(msg)

    def __gt__(self: Self, other: Self) -> bool:
        if self.type_ > other.type_:
            return True
        if self.type_ < other.type_:
            return True
        for self_card, other_card in zip(self.cards, other.cards, strict=True):
            if self.strength_order.index(self_card) > self.strength_order.index(
                other_card,
            ):
                return True
            if self.strength_order.index(self_card) < self.strength_order.index(
                other_card,
            ):
                return False
        msg = "Hands are equal"
        raise ValueError(msg)


def part1(hands: list[Hand]) -> int:
    return sum(hand.bid * index for index, hand in enumerate(sorted(hands), start=1))


def part2(hands: list[Hand]) -> int:
    return sum(hand.bid * index for index, hand in enumerate(sorted(hands), start=1))


if __name__ == "__main__":
    raw_text = Path("../input.txt").read_text()
    hands = [Hand.from_text(line) for line in raw_text.split("\n") if line]
    hands_but_with_jokers = [
        Hand.from_text(line, using_jokers=True) for line in raw_text.split("\n") if line
    ]
    print(part1(hands))
    print(part2(hands_but_with_jokers))
