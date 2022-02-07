#
from typing import Optional


def to_power(x: Optional[int | float], exp: int) -> Optional[int | float]:
    if exp == 1:
        return x
    else:
        return x * to_power(x, exp - 1)


print(to_power(2, 4))


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) < 2:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:])


print(is_palindrome('sassas'))


def mult(a: int, n: int) -> int:
    if n == 1:
        return a
    if n == 0:
        return 0
    else:
        return a + mult(a, n - 1)


print(mult(2, 10))


def sum_of_digits(digit_string: str) -> int:
    if digit_string == '':
        return 0
    else:
        return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits("2222"))


def reverse(input_str: str) -> str:
    if input_str == '':
        return input_str
    if len(input_str) == 1:
        return input_str
    else:
        return input_str[-1] + reverse(input_str[:-1])


print(reverse("lololo"))
