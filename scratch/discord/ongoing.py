from collections import defaultdict


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
