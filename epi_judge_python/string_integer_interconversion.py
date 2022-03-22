from test_framework import generic_test
from test_framework.test_failure import TestFailure

# 3/22/2022
# Helper function convert string to int
def digit_string_to_int(c):  # character
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
def digit_int_to_string(d):  # character
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
def int_to_string(x: int) -> str:  # does not have to worry about the sign of +
    # Set Flag and result
    flag = ""
    result = ""
    if x == 0:
        return "0"
    if x < 0:
        flag = "-"

    # Go through each number, extract and concat to number, then delete it from int
    x = abs(x)
    while x:
        # extract the last digit, aka remainder
        last_digit = x % 10

        # append the converted digit
        result += digit_int_to_string(last_digit)

        # delete last digit
        x //= 10

    # concat flag
    result += flag

    # reverse string
    result = result[::-1]

    return result

    # Time Complexity: O(n) due to while loop
    # Space Complexity: O(1) due to not using any extra space


def string_to_int(s: str) -> int:
    # Set flag
    flag = 0
    result = 0

    if s[0] == "+":
        flag = 1
    elif s[0] == "-":
        flag = -1
    else:  # just number
        flag = 1

    # Go through each number with for loop, add that number and shift and multiply by 10
    for i in range(0, len(s)):
        result *= 10
        result += digit_string_to_int(s[i])

    return flag * result

    # Time Complexity: O(n) due to while loop
    # Space Complexity: O(1) due to not using any extra space


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
