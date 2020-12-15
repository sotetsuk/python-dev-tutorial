.PHONY: pytest install uninstall clean check

pytest:
	pytest --doctest-modules

install:
	python3 setup.py install 

check:
	mypy fizzbuzz

uninstall:
	pip3 uninstall fizzbuzz -y

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*pycache*" | xargs rm -rf
