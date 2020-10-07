from unittest import TestCase
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(2), "2")
