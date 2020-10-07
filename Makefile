.PHONY: unittest doctest

unittest:
	python3 -m unittest discover -v

doctest:
	python3 -m doctest -v fizzbuzz/*.py
