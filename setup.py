from setuptools import setup, find_packages

setup(
    name='fizzbuzz',
    version="0.0.1",
    description='Fizz Buzz program.',
    author='sotetsuk',
    url='https://github.com/sotetsuk/python-dev-tutorial',
    author_email='koyamada-s@sys.i.kyoto-u.ac.jp',
    license='MIT',
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)
