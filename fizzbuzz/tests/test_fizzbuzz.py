import pytest
from fizzbuzz.fizzbuzz import fizzbuzz

fizzbuzz_data = [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (2, "2")]
fizzbuzz_7_11_data = [(7, "Fizz"), (11, "Buzz"), (77, "FizzBuzz"), (5, "5")]


@pytest.mark.parametrize(('n', 'expected'), fizzbuzz_data)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected


@pytest.mark.parametrize(('n', 'expected'), fizzbuzz_7_11_data)
def test_fizzbuzz_7_11(n, expected):
    assert fizzbuzz(n, fizz=7, buzz=11) == expected
