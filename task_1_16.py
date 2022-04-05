# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
# "add called with 4, 5"
from functools import wraps


def logger(func):
    @wraps(func)
    def print_f(*args):
        func_args = ','.join([str(i) for i in args])
        print(f'{func.__name__} called with {func_args}')

    return print_f


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


def main():
    add(5, 7)
    square_all(4, 8, 5)


if __name__ == '__main__':
    main()
