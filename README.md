# python-dev-tutorial

Pythonを用いた開発トレーニングの資料

---

# fizzbuzz

![tests](https://github.com/sotetsuk/python-dev-tutorial/workflows/tests/badge.svg)

A [Fizz Buzz](https://ja.wikipedia.org/wiki/Fizz_Buzz) program available as Python package and CLI tool.

## How to install

```sh
$ make install
```

## Usage as Python package

`fizzbuzz` function can transform a number following the Fizz Buzz rule.

```py
>>> from fizzbuzz.fizzbuzz import fizzbuzz
>>> fizzbuzz(3)
'Fizz'
>>> fizzbuzz(5)
'Buzz'
>>> fizzbuzz(15)
'FizzBuzz'
>>> fizzbuzz(2)
'2'
```

## Usage as CLI tool

`fizzbuzz-cli` can receive any number of arguments.

```sh
$ fizzbuzz-cli 3 5 15 2
Fizz
Buzz
FizzBuzz
2
```

If no arguments are passed, it receives numbers from stdin.

```sh
$ seq 1 100 | fizzbuzz-cli
1
2
Fizz
...
```

See help message for further usage.

```sh
$ fizzbuzz-cli --help                                                                                                                                                                                                                                                                                       (sotetsuk/docs/readme✱)
Usage: fizzbuzz-cli [OPTIONS] [NUMS]...

  Fizz Buzz program. If no arguments are passed, it reads numbers from
  stdin.")

Options:
  --fizz INTEGER  Number corresponds to Fizz.
  --buzz INTEGER  Number corresponds to Buzz.
  --help          Show this message and exit.
```

## LICENSE
MIT License

