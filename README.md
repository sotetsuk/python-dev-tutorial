# python-dev-tutorial

このリポジトリは、Pythonを用いた開発トレーニングの資料です。
想定読者は、Pythonの文法やGitの使い方は一通り勉強したが、実際の開発経験があまりない方を想定しています（学部生など）。

目次に沿って読み進めながら、このリポジトリの内容を再構築することで、開発において重要な次のスキルが身につくと想定しています。

1. **Issue/PRベースのGitHub上での開発の仕方**
2. **ユニットテストを使った開発の仕方**
3. **CIを使った開発の進め方**
4. **Pythonコードのパッケージングの仕方**
5. **PythonコードのCLIツールとしての切り出し方**

## 目次

1. [プロジェクトを初期化しよう](https://github.com/sotetsuk/python-dev-tutorial/issues/1)
2. [仕様を決めて、ユニットテストを追加してみよう](https://github.com/sotetsuk/python-dev-tutorial/issues/3)
3. [ユニットテストが通るように本体を実装してみよう](https://github.com/sotetsuk/python-dev-tutorial/issues/5)
4. [(Optional) doctestを導入してみよう](https://github.com/sotetsuk/python-dev-tutorial/issues/7)
5. [新しい機能を追加する前に、CIを導入してみよう](https://github.com/sotetsuk/python-dev-tutorial/issues/9)
6. [新しい機能を追加してみよう](https://github.com/sotetsuk/python-dev-tutorial/issues/11)
7. [ライブラリとして使えるようにしてみよう](https://github.com/sotetsuk/python-dev-tutorial/issues/13)
8. [CLIツールとして使えるようにしてみよう](https://github.com/sotetsuk/python-dev-tutorial/issues/15)
9. [(Optional) 便利な外部ライブラリをインストールして使ってみよう (Pytest編)](https://github.com/sotetsuk/python-dev-tutorial/issues/17)
10. [(Optional) 便利な外部ライブラリをインストールして使ってみよう (Click編)](https://github.com/sotetsuk/python-dev-tutorial/issues/19)
11. [しっかりとしたREADMEを書こう](https://github.com/sotetsuk/python-dev-tutorial/issues/22)

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

