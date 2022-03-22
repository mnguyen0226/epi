from test_framework import generic_test

# 3/9/2022
# Write a program that takes a 640bit unsigned integer and returns the 64-bit unsigned integer consisting of the bits of the input in reverse order.
# Solution: shift the result to the left, get the last bit of the input, then or the 0 with the last bit
def reverse_bits(x: int) -> int:
    result = 0
    size = 64
    for i in range(size):
        result <<= 1
        result |= (x >> i) & 0x1
    return result

    # Time Complexity: O(1)
    # Space Complexity: O(1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_bits.py", "reverse_bits.tsv", reverse_bits
        )
    )
