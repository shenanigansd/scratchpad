from collections import defaultdict

import pytest


# https://discord.com/channels/267624335836053506/587375768556797982/1044549320948584528
def keychain(dicts: list[dict]) -> dict:
    """Create a dict of chains of keys from sequential dicts"""
    output = defaultdict(list)

    first, *dicts = dicts
    for key, value in first.items():
        output[key].append(value)

    for dct in dicts:
        for key, value in output.items():
            last_value = value[-1]
            output[key].append(dct[last_value])

    return output


def test_keychain():
    """test: keychain"""
    dicts = [
        {"a": "b", "v": "w", "o": "p"},
        {"b": "c", "w": "x", "p": "q"},
        {"c": "d", "x": "y", "q": "r"},
    ]

    new_dict = {"a": ["b", "c", "d"], "v": ["w", "x", "y"], "o": ["p", "q", "r"]}

    assert keychain(dicts) == new_dict


# https://discord.com/channels/267624335836053506/267624335836053506/1047647967143792661
def range_parser(text: str) -> list[int]:
    output = []
    text = text.replace(" ", "")
    items = text.split(",")
    for item in items:
        if "-" in item:
            start, stop = item.split("-")
            output.extend(list(range(int(start), int(stop) + 1)))
        else:
            output.append(int(item))
    return output


@pytest.mark.parametrize(
    "value,result",
    [
        ("5 - 8", [5, 6, 7, 8]),
        ("5, 7, 10", [5, 7, 10]),
        ("5, 7-10", [5, 7, 8, 9, 10]),
    ],
)
def test_range_parser(value: str, result: list[int]):
    assert range_parser(value) == result
