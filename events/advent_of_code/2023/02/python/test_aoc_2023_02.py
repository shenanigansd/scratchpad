import pytest
from aoc_2023_02 import Dice, Game, SetOfDice


@pytest.mark.parametrize(
    ("text", "game"),
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            Game(
                1,
                [
                    SetOfDice([Dice("blue", 3), Dice("red", 4)]),
                    SetOfDice([Dice("red", 1), Dice("green", 2), Dice("blue", 6)]),
                    SetOfDice([Dice("green", 2)]),
                ],
            ),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            Game(
                2,
                [
                    SetOfDice([Dice("blue", 1), Dice("green", 2)]),
                    SetOfDice([Dice("green", 3), Dice("blue", 4), Dice("red", 1)]),
                    SetOfDice([Dice("green", 1), Dice("blue", 1)]),
                ],
            ),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            Game(
                3,
                [
                    SetOfDice([Dice("green", 8), Dice("blue", 6), Dice("red", 20)]),
                    SetOfDice([Dice("blue", 5), Dice("red", 4), Dice("green", 13)]),
                    SetOfDice([Dice("green", 5), Dice("red", 1)]),
                ],
            ),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            Game(
                4,
                [
                    SetOfDice([Dice("green", 1), Dice("red", 3), Dice("blue", 6)]),
                    SetOfDice([Dice("green", 3), Dice("red", 6)]),
                    SetOfDice([Dice("green", 3), Dice("blue", 15), Dice("red", 14)]),
                ],
            ),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            Game(
                5,
                [
                    SetOfDice([Dice("red", 6), Dice("blue", 1), Dice("green", 3)]),
                    SetOfDice([Dice("blue", 2), Dice("red", 1), Dice("green", 2)]),
                ],
            ),
        ),
    ],
)
def test_parsing_data(text: str, game: Game) -> None:
    assert Game.from_row(text) == game


@pytest.mark.parametrize(
    ("game", "minimums"),
    [
        (
            Game(
                1,
                [
                    SetOfDice([Dice("blue", 3), Dice("red", 4)]),
                    SetOfDice([Dice("red", 1), Dice("green", 2), Dice("blue", 6)]),
                    SetOfDice([Dice("green", 2)]),
                ],
            ),
            (4, 2, 6),
        ),
        (
            Game(
                2,
                [
                    SetOfDice([Dice("blue", 1), Dice("green", 2)]),
                    SetOfDice([Dice("green", 3), Dice("blue", 4), Dice("red", 1)]),
                    SetOfDice([Dice("green", 1), Dice("blue", 1)]),
                ],
            ),
            (1, 3, 4),
        ),
        (
            Game(
                3,
                [
                    SetOfDice([Dice("green", 8), Dice("blue", 6), Dice("red", 20)]),
                    SetOfDice([Dice("blue", 5), Dice("red", 4), Dice("green", 13)]),
                    SetOfDice([Dice("green", 5), Dice("red", 1)]),
                ],
            ),
            (20, 13, 6),
        ),
        (
            Game(
                4,
                [
                    SetOfDice([Dice("green", 1), Dice("red", 3), Dice("blue", 6)]),
                    SetOfDice([Dice("green", 3), Dice("red", 6)]),
                    SetOfDice([Dice("green", 3), Dice("blue", 15), Dice("red", 14)]),
                ],
            ),
            (14, 3, 15),
        ),
        (
            Game(
                5,
                [
                    SetOfDice([Dice("red", 6), Dice("blue", 1), Dice("green", 3)]),
                    SetOfDice([Dice("blue", 2), Dice("red", 1), Dice("green", 2)]),
                ],
            ),
            (6, 3, 2),
        ),
    ],
)
def test_parsing_data(game: Game, minimums: tuple[int]) -> None:
    assert game.minimum_per_color() == minimums
