"""Testing the fizzbuzz function"""

from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    """Testing the fizzbuzz function"""
    lst = list(fizzbuzz(100, [(3, "Fizz"), (5, "Buzz")]))

    assert lst[0] == "1"
    assert lst[2] == "Fizz"
    assert lst[4] == "Buzz"
    assert lst[14] == "FizzBuzz"
