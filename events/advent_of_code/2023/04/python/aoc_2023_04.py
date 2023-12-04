from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Card:
    id_number: int
    numbers: list[int]
    winning_numbers: list[int]

    @classmethod
    def from_text(cls, text: str):
        header, body = text.split(":")
        id_number = int(header.split(" ")[-1])
        winning_numbers_text, numbers_text = body.split("|")
        winning_numbers = [int(number) for number in winning_numbers_text.split(" ") if number]
        numbers = [int(number) for number in numbers_text.split(" ") if number]
        return cls(id_number, numbers, winning_numbers)

    def winning_number_count(self) -> int:
        return sum(1 for number in self.numbers if number in self.winning_numbers)

    def points(self) -> int:
        count = self.winning_number_count()
        total = 0
        if count > 0:
            total = 1
        for _ in range(count - 1):
            total *= 2
        return total


@dataclass(frozen=True)
class Deck:
    cards: list[Card]

    @classmethod
    def from_cards(cls, cards: list[Card]):
        return cls(cards)

    def count_new_cards(self) -> int:
        cards_per_card = {
            card.id_number: list(range(card.id_number + 1, card.id_number + card.winning_number_count()))
            for card in self.cards
        }
        for key, value in cards_per_card.items():
            new_cards = [value.copy()]
            while True:
                new_cards.append([number for val in new_cards[-1] for number in cards_per_card[val]])
                if new_cards[-1] == []:
                    new_cards.pop()
                    cards_per_card[key] = sum(item for lst in new_cards for item in lst)
                    break
        return sum(cards_per_card.values())


def part1(cards: list[Card]) -> int:
    return sum(card.points() for card in cards)


def part2(cards: list[Card]) -> int:
    deck = Deck(cards)
    return deck.count_new_cards()


if __name__ == "__main__":
    raw_rows = Path("../input.txt").read_text().split("\n")
    cards = [Card.from_text(row) for row in raw_rows]
    print(part1(cards))
    print(part2(cards))
