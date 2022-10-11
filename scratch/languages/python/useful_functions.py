"""Assorted utility functions"""

import json
import random
import re
import string
from typing import Any, Generator, Iterable


# https://stackoverflow.com/a/18860653
def dict_compare(
    old_dict: dict[Any, Any], new_dict: dict[Any, Any]
) -> tuple[list[Any], list[Any], dict[Any, Any], list[Any]]:
    """
    Compare two different dictionaries.

    Parameters
    ----------
    old_dict : dict[Any, Any]
        The old dictionary
    new_dict : dict[Any, Any]
        The new dictionary

    Returns
    -------
    Comparison results : (list[Any], list[Any], dict[Any, Any], list[Any])

    Examples
    --------
    >>> dict_compare(old_dict=dict(), new_dict=dict())
    (list(), list(), dict(), list())
    """
    old_dict_keys: set[Any] = set(old_dict.keys())
    new_dict_keys: set[Any] = set(new_dict.keys())
    intersecting_keys: set[Any] = old_dict_keys.intersection(new_dict_keys)
    new_keys: set[Any] = new_dict_keys - old_dict_keys
    removed_keys: set[Any] = old_dict_keys - new_dict_keys
    modified_keys: dict[Any, tuple[Any, Any]] = {
        key: (old_dict[key], new_dict[key])
        for key in intersecting_keys
        if old_dict[key] != new_dict[key]
    }
    unmodified_keys: set[Any] = set(
        o for o in intersecting_keys if old_dict[o] == new_dict[o]
    )
    return list(new_keys), list(removed_keys), modified_keys, list(unmodified_keys)


# https://stackoverflow.com/a/24290026/8160821
def enumerate2(
    xs: Iterable[Any], start: int = 0, step: int = 1
) -> Generator[tuple[int, Any], Any, None]:
    """
    Yield items from a list with a custom index.

    Yields
    ------
    item, index : tuple[Any, int]
        The next item and the next number per step
    """
    for x in xs:
        yield start, x
        start += step


# https://stackoverflow.com/a/312464/8160821
def chunks(lst: list[Any], n: int) -> Generator[list, Any, None]:
    """
    Yield successive n-sized chunks from lst.

    Yields
    ------
    chunk : list
        An n-sized chunk of the list
    """
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# https://stackoverflow.com/a/952952
def flatten(lst: list[list[Any]]) -> list[Any]:
    """
    Flattens a list of lists into a single list.

    Parameters
    ----------
    lst : list[list[Any]]
        The nested lists to flatten.

    Returns
    -------
    flattend_list : list[Any]
        The flattened list.

    Examples
    --------
    >>> flatten(lst=[['a'],['b']])
    ['a', 'b']
    """
    return [item for sublist in lst for item in sublist]


def random_string(length: int = 6, characters: str = string.ascii_uppercase) -> str:
    """
    Generates a random string of the specified length using the specified character set.

    Parameters
    ----------
    length
        The desired length.
    characters
        The character set.

    Returns
    -------
    result : str
        A random string.

    Examples
    --------
    >>> random_string(length=1,  characters='a')
    'a'
    """
    return "".join(random.choices(characters, k=length))


def split_prefix_and_number(text: str) -> tuple[str, int]:
    """
    Split a string into alpha prefix and numeric suffix.

    Parameters
    ----------
    text : str
        The text to split

    Returns
    -------
    prefix, number : tuple[str, int]
        The prefix and the number

    Examples
    --------
    >>> split_prefix_and_number('U1500000')
    ('U', 1500000)
    """
    search_results = re.search(r"([a-zA-Z])(\d+)", text)

    if search_results is None:
        raise ValueError("Invalid input")

    prefix, number = search_results.groups()

    return prefix, int(number)


class CustomEncoder(json.JSONEncoder):
    """A custom JSON encoder that attempts to convert all user defined classes to string."""

    def default(self, obj: Any) -> Any:
        """
        Serialize an object.
        If the object is not a builtin, return the __str__ of the object.
        For builtins, use the standard serializer.

        Parameters
        ----------
        obj : Any
            Object to serialize

        Returns
        -------
        serialized_object : Any
            Serialized object
        """
        if type(obj) not in [dict, list, tuple, str, int, float, bool, None]:
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def find_nth(haystack: str, needle: str, n: int) -> int:
    """
    Find the nth occurrence of a substring in a string.

    Parameters
    ----------
    haystack
        The string to search in
    needle
        The substring to search for
    n
        Which nth occurrence to find

    Returns
    -------
    The index of the nth occurrence of the substring, or -1 if not found.

    Examples
    --------
    >>> find_nth("yankee doodle", "o", 2)
    9
    """
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def bulk_substring_remove(text: str, substrings: list[str]):
    """
    Remove all substrings from a string.

    Parameters
    ----------
    text
        The string to update
    substrings
        The substrings to remove

    Returns
    -------
    The original string with all substrings removed

    Examples
    --------
    >>> bulk_substring_remove("yankee doodle", ["yan", "dle"])
    "kee doo"
    """
    for substring in substrings:
        text = text.replace(substring, "")
    return text


def get_nested_dict_value(
    dct: dict, keypath: str, default=None, separator: str = "."
) -> Any:
    """
    Parse nested values from dictionaries

    Parameters
    ----------
    dct
        The dictionary to search
    keypath
        The path of keys to check through
    default
        The default value to return if the value is not found
    separator
        The character used to split the keypath

    Returns
    -------
    The value at the keypath or the default value

    Examples
    --------
    >>> get_nested_dict_value({"key": {"path": "value"}}, "key.path")
    "value"
    """
    keys = keypath.split(separator)

    value = dct
    for key in keys:
        value = value.get(key)

        if not value:
            value = default
            break

    return value
