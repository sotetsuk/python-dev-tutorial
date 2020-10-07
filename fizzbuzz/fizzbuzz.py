import argparse
import sys


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


def main():
    parser = argparse.ArgumentParser(description='Fizz Buzz program.')
    parser.add_argument('nums', type=int, default=[], nargs='*',
                        help="Numbers to be applied to FizzBuzz function. If no arguments passed, read from stdin.")
    parser.add_argument('--fizz', type=int, default=3,
                        help='Number corresponds to Fizz.')
    parser.add_argument('--buzz', type=int, default=5,
                        help='Number corresponds to Buzz.')
    args = parser.parse_args()

    if args.nums:  # 数字の列が引数から渡された場合には、それらの数字にFizzBuzzを適用する
        sys.stderr.write("Reading numbers from arguments ...\n")
        for n in args.nums:
            sys.stdout.write(f"{fizzbuzz(n, fizz=args.fizz, buzz=args.buzz)}\n")
    else:  # 数字の列が引数から渡されなかった場合には、標準入力から数字を読み込む
        sys.stderr.write("Reading numbers from stdin ...\n")
        try:
            line = sys.stdin.readline()
            while line:
                sys.stdout.write(f"{fizzbuzz(int(line), fizz=args.fizz, buzz=args.buzz)}\n")
                line = sys.stdin.readline()
        except KeyboardInterrupt:
            return
