def fizzbuzz(n: int, fizz: int = 3, buzz: int = 5) -> str:
    """Fizz Buzz function.

    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(2)
    '2'
    """
    if n % fizz == 0 and n % buzz == 0:
        return "FizzBuzz"
    elif n % fizz == 0:
        return "Fizz"
    elif n % buzz == 0:
        return "Buzz"
    else:
        return str(n)
