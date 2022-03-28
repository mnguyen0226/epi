from test_framework import generic_test

# 3/9/2022
# Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j

# Time complexity: O(1) since the calculation is independent of word size
# Space complexity: O(1)
def swap_bits(x, i, j):
    # Check if the bit at i and j are similar, if they arem ther swap will not change any values
    if (x >> i & 1) != (x >> j & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask  # XOR any bit with 1 will flip the value

    return x


# 3/13/2022
# Brute-force: Check if the bit at position i and j are the same, if they are, we can bit mask and flip the bit
def swap_bit_review(x, i, j):
    # Get the bit at index i and j, then compare them with right shift
    if (x >> i & 1) != (x >> j & 1):

        # get bit mask with left shift
        bit_mask = (1 << i) | (1 << j)

        # flip bits with XOR with 1
        x ^= bit_mask

    return x

    # Time Complexity: O(1)
    # Space Complexity: O(1)


# 3/27/2022
def swap_bit_review_2(x, i, j):
    # Get the digit at position i and j
    digit_i = x >> i
    digit_j = x >> j
    if digit_i == digit_j:
        return x
    else:
        mask_i = 1 << i
        mask_j = 1 << j
        x = x ^ mask_i
        x = x ^ mask_j
        return x

    # Time Complexity: O(1): single number
    # Space Complexity: O(1): Not using any extra space


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "swap_bits.py", "swap_bits.tsv", swap_bit_review_2
        )
    )
