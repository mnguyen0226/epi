from math import remainder
from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

# 3/22/2022
# Helper function convert string to int
def char_to_digit(c):  # character
    if c == "0":
        return 0
    elif c == "1":
        return 1
    elif c == "2":
        return 2
    elif c == "3":
        return 3
    elif c == "4":
        return 4
    elif c == "5":
        return 5
    elif c == "6":
        return 6
    elif c == "7":
        return 7
    elif c == "8":
        return 8
    elif c == "9":
        return 9
    else:  # either + or -
        return 0


# Helper function convert int to string
def digit_to_char(d):  # character
    if d == 0:
        return "0"
    elif d == 1:
        return "1"
    elif d == 2:
        return "2"
    elif d == 3:
        return "3"
    elif d == 4:
        return "4"
    elif d == 5:
        return "5"
    elif d == 6:
        return "6"
    elif d == 7:
        return "7"
    elif d == 8:
        return "8"
    elif d == 9:
        return "9"


# 3/21/2022
def int_to_string(x: int) -> str:
    # base case, the while loop won't work if we got "while 0"
    if x == 0:
        return "0"

    # check flag
    flag_posi = True
    if x < 0:
        flag_posi = False

    new_string = ""

    # get rid of sign
    x = abs(x)

    # keep + the last character to the new string
    while x:
        remainder = x % 10
        x = x // 10  # get rid of remainder, floor divider
        new_string += chr(ord("0") + remainder)

    if flag_posi == False:
        new_string += "-"

    # reverse it
    new_string = new_string[::-1]

    return new_string

    # T: O(n)
    # S: O(1)


def string_to_int(s: str) -> int:  # no base case for string to int
    new_int = 0
    i = 0

    # Check flag
    flag_posi = True
    if s[0] == "-":
        flag_posi = False

    # Avoid - or + sign
    if s[i] == "-" or s[i] == "+":
        i = 1

    for i in range(i, len(s)):
        new_int = new_int + string.digits.index(s[i])
        if i == len(s) - 1:
            break
        new_int *= 10

    if flag_posi == False:
        new_int *= -1

    return new_int

    # T: O(n)
    # S: O(1)


# 5/21/2022
def int_to_string2(x: int) -> str:
    # check for 0 because while can't deal with it
    if x == 0:
        return "0"

    is_neg = False
    if x < 0:
        is_neg = True

    # get absolute
    x = abs(x)
    s = ""

    while x:
        remainder = x % 10
        remainder = chr(ord("0") + remainder)  # convert int to char
        x = x // 10  # floor div
        s = s + remainder

    if is_neg:
        s = s + "-"

    return s[::-1]


def string_to_int2(s: str) -> int:
    if s is None:
        return None

    i = 0
    x = 0

    is_neg = False
    if s[0] == "-":
        i = 1
        is_neg = True
    elif s[0] == "+":
        i = 1

    for j in range(i, len(s)):
        num = string.digits.index(s[j])
        x = x * 10
        x += num

    if is_neg:
        x = -x

    return x

    # T: O(n)
    # S: O(1)


# 6/2/2022
def int_to_string3(x: int) -> str:
    if x == 0:
        return "0"

    str_num = ""
    is_neg = False

    if x < 0:
        is_neg = True

    x = abs(x)

    while x:
        remainder = x % 10
        str_num = str_num + chr(ord("0") + remainder)
        x = x // 10  # get rid of the remainder

    if is_neg:
        str_num += "-"

    return str_num[::-1]


import string


def string_to_int3(s: str) -> int:
    int_num = 0
    has_sign = 0

    if s[0] == "+" or s[0] == "-":
        has_sign = 1

    for i in range(has_sign, len(s)):
        int_num = int_num * 10 + string.digits.index(s[i])

    if has_sign == 1 and s[0] == "-":
        int_num = -int_num

    return int_num


# def int_to_string(x: int) -> str:
#     return None
# def string_to_int(s: str) -> int:
#     return 0


def wrapper(x, s):
    if int(int_to_string3(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int3(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
