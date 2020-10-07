from unittest import TestCase
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(2), "2")

        # fizz = 7, buzz = 11
        self.assertEqual(fizzbuzz(7, fizz=7, buzz=11), "Fizz")
        self.assertEqual(fizzbuzz(11, fizz=7, buzz=11), "Buzz")
        self.assertEqual(fizzbuzz(77, fizz=7, buzz=11), "FizzBuzz")
        self.assertEqual(fizzbuzz(5, fizz=7, buzz=11), "5")
