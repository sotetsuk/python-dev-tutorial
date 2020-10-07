.PHONY: unittest doctest install uninstall clean

unittest:
	python3 -m unittest discover -v

doctest:
	python3 -m doctest -v fizzbuzz/*.py

install:
	python3 setup.py install 

uninstall:
	pip3 uninstall fizzbuzz -y

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*pycache*" | xargs rm -rf
