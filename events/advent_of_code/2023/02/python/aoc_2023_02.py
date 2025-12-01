from dataclasses import dataclass
from math import prod
from pathlib import Path

CRITERION = {"red": 12, "green": 13, "blue": 14}


@dataclass(frozen=True)
class Dice:
    color: str
    quantity: int


@dataclass(frozen=True)
class SetOfDice:
    dice: list[Dice]

    @classmethod
    def from_str(cls, text: str) -> SetOfDice:
        dice = []
        dice_chunks = text.split(",")
        for dice_chunk in dice_chunks:
            quantity, color = dice_chunk.strip().split(" ")
            dice.append(Dice(color, int(quantity)))
        return cls(dice)


@dataclass(frozen=True)
class Game:
    game_id: int
    sets: list[SetOfDice]

    @classmethod
    def from_row(cls, row: str) -> Game:
        game_id_text, dice_sets = row.split(":")
        game_id = int(game_id_text[5:])
        sets = [SetOfDice.from_str(dice_set) for dice_set in dice_sets.split(";")]
        return cls(game_id, sets)

    def minimum_per_color(self) -> tuple[int]:
        dice_per_color = {"red": [], "green": [], "blue": []}
        for sets in self.sets:
            for dice in sets.dice:
                dice_per_color[dice.color].append(dice.quantity)
        return tuple(max(dice_per_color[color]) for color in dice_per_color)


def part1(games: list[Game]) -> int:
    return sum(
        game.game_id
        for game in games
        if all(
            dice.color in CRITERION and dice.quantity <= CRITERION[dice.color]
            for sets in game.sets
            for dice in sets.dice
        )
    )


def part2(games: list[Game]) -> int:
    return sum(prod(game.minimum_per_color()) for game in games)


if __name__ == "__main__":
    raw_rows = Path("../input.txt").read_text(encoding="locale").split("\n")
    rows = [Game.from_row(row) for row in raw_rows]
    print(part1(rows))
    print(part2(rows))
