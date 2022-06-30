"""Example FizzBuzz snippet"""


def fizzbuz(number: int, cases: list[tuple[int, str]]):
    """
    For each number between one and `number`,
    loop through the cases and return a concatenated string of
    the text where the case is divisible by zero,
    or the original number if no cases were divisible.
    """
    for index in range(1, number + 1):
        output = ""
        for divisor, text in cases:
            if index % divisor == 0:
                output += text
        if output == "":
            output = index
        print(output)


if __name__ == '__main__':
    fizzbuz(100, [(3, "Fizz"), (5, "Buzz")])
