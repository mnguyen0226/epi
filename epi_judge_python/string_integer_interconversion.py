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
        x = x // 10 # get rid of remainder, floor divider
        new_string += chr(ord('0') + remainder) 
    
    
    if flag_posi == False:
        new_string += '-'
        
    # reverse it 
    new_string = new_string[::-1]
    
    return new_string

    # T: O(n)
    # S: O(1)
    
def string_to_int(s: str) -> int: # no base case for string to int
    new_int = 0
    i = 0

    # Check flag
    flag_posi = True
    if s[0] == '-':
        flag_posi = False
    
    # Avoid - or + sign
    if s[i] == '-' or s[i] == '+':
        i = 1
    
    for i in range(i, len(s)):
        new_int = (new_int + string.digits.index(s[i])) 
        if i == len(s) - 1:
            break
        new_int *= 10
    
    if flag_posi == False:
        new_int *= -1
        
    return new_int

    # T: O(n)
    # S: O(1)

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
