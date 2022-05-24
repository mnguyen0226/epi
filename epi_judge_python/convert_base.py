import functools
from math import remainder
import string
from test_framework import generic_test

# Helper function that convert int to letter
def int_to_letter(i):
    if i == 10:
        return "A"
    elif i == 11:
        return "B"
    elif i == 12:
        return "C"
    elif i == 13:
        return "D"
    elif i == 14:
        return "E"
    elif i == 15:
        return "F"


# Helper function that convert letter to int
def letter_to_int(l):
    if l == "A":
        return 10
    elif l == "B":
        return 11
    elif l == "C":
        return 12
    elif l == "D":
        return 13
    elif l == "E":
        return 14
    elif l == "F":
        return 15


# 3/16/2022
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # Case 1: when the string is 0 then the return string is also 0
    if num_as_string == "0":
        return "0"

    # Check negative
    is_negative = 0
    if num_as_string[0] == "-":
        is_negative = 1

    # S1: Convert string base 1 to int in decimal by multiplication and add
    res_int_base_1 = 0
    power = 0

    # Go through each index of string backward and with the incrementation of power
    for i in reversed(range(is_negative, len(num_as_string))):
        digit = num_as_string[i]  # this is a char

        # convert the letter to int and multiply with power
        if (
            digit == "A"
            or digit == "B"
            or digit == "C"
            or digit == "D"
            or digit == "E"
            or digit == "F"
        ):
            digit = letter_to_int(digit)
            res_int_base_1 += digit * pow(b1, power)
        else:
            res_int_base_1 += int(digit) * pow(b1, power)
        power += 1

    # S2: Convert int in decimal to string base 2 with mod and floor division
    str_base_2 = ""

    # go through each character of int
    while res_int_base_1:
        # get the last digit

        last_digit = res_int_base_1 % b2
        # convert the last digit to letter
        if last_digit >= 10 and last_digit <= 15:
            last_digit = int_to_letter(last_digit)
            str_base_2 += last_digit

        else:
            str_base_2 += str(last_digit)

        # remove the last digit with base 2
        res_int_base_1 //= b2

    # Append negative sign
    if is_negative == 1:
        str_base_2 += "-"

    # Reverse the string
    str_base_2 = str_base_2[::-1]

    return str_base_2

    # Time Complexity: O(n) since using loop through characters of the string
    # Space Complexity: O(n) since using a new string to store the new digit at a time


# 5/24/2022
def convert_base2(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(num_as_int, base):
        if num_as_int == 0:
            return ""
        return (
            construct_from_base(num_as_int // base, base)
            + string.hexdigits[num_as_int % base].upper()
        )

    is_neg = num_as_string[0] == "-" # true is 1
    
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()), # function/operator - convert each character to number and x is 0 initizer
        num_as_string[is_neg:], # go through all character
        0, # initial value is 0
    )
        
    return ("-" if is_neg else "") + (
        "0" if num_as_int == 0 else construct_from_base(num_as_int, b2)
    )

    # T: O(n)
    # S: O(1)

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base2
        )
    )
