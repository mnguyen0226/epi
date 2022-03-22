from tabnanny import check
from test_framework import generic_test

# Time Complexity: O(n) since run through all the bits
# Space Complexity: O(1) since not use any data structure to store values
def parity(x: int) -> int:
    # Count number of bits
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1

    # Parity check
    parity = 0
    if num_bits % 2 == 0:
        parity = 0
    else:
        parity = 1

    return parity


# Time Complexity: O(n) since run through all the bits
# Space Complexity: O(1) since not use any data structure to store values
def parity_2(x: int) -> int:
    result = 0
    while x:  # Here: The XOR of the group of bits is its parity
        result ^= x & 1
        x >>= 1
    return result


# assuming that the input is 64 bits
# XOR property: association, the XOR of the group of bits is its parity
# Time Complexity: O(logn) since run through all the bits
# Space Complexity: O(1) since not use any data structure to store values
def parity_3(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1  # get the last bit
    x &= 0x1  # extract last bit as int
    return x


# Review: 3/13/2022
# Write a program to check the parity of an 64-bits int
# Solution: go through a number, coun number of bits then check if it is odd or even
def parity_review_1a(x):
    num_bits = 0
    check_parity = 0

    # Go count the number of 1s in the last bit and shift the number to the right
    while x:
        num_bits += x & 1  # get the last bit, return 1 if the last bit is 1, else 0
        x >>= 1

    # Check odd or reven
    check_parity = 1 if (num_bits % 2) == 1 else 0

    return check_parity

    # Time Complexity: O(n) since we have to go through all the bits
    # Space Complexity: O(1) since we don't use any data structure to store data


# Parity Rule: The parity of a number equal to XOR the last bit to with 1
def parity_review_1b(x):
    check_parity = 0
    while x:
        check_parity ^= x & 1
        x >>= 1
    return check_parity

    # Time Complexity: O(n)
    # Space Complexity: O(1)


# Parity Rule: x&(x - 1) = erase the lowest bit set
# We chop the last bit 1 everytime and replace with 0, the parity will toggle 1 and 0, if the number of 1s (aka number of toggle is odd), thenn the result is 1
def parity_review_1c(x):
    check_parity = 0
    while x:
        check_parity ^= 1
        x &= x - 1
    return check_parity

    # Time Complexity: O(k) with k is the number of 1s
    # Space Complexity: O(1)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("parity.py", "parity.tsv", parity_review_1c))
