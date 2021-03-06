"""Example FizzBuzz snippet"""

from collections.abc import Iterator


def fizzbuzz(number: int, cases: list[tuple[int, str]]) -> Iterator[str]:
    """
    For each number between one and `number`,
    loop through the cases and yield a concatenated string of
    the text where the case is divisible by zero,
    or the original number if no cases were divisible.
    """
    for index in range(1, number + 1):
        output = ""
        for divisor, text in cases:
            if index % divisor == 0:
                output += text
        if output == "":
            output = str(index)
        yield output


if __name__ == "__main__":
    lst = list(fizzbuzz(100, [(3, "Fizz"), (5, "Buzz")]))

    assert lst[0] == "1"
    assert lst[2] == "Fizz"
    assert lst[4] == "Buzz"
    assert lst[14] == "FizzBuzz"

    for item in lst:
        print(item)
