# 3/9/2022
# Write a program that count the number of bits that are set to 1 in a positive integer
# Analysis:
# - Time Complexity: O(n) per bit
# - Space Complexity: O(1) since we don't use any data structure for storage


def count_bits(x):
    # Initialize the number of 1
    num_bits = 0

    # Go through all the bit in an int
    while x:
        num_bits += (
            x & 1
        )  # AND logic gate: if the last bit and 1 has the same bit then return 1
        x >>= 1  # shift right by 1 bit
    return num_bits


def main():
    num = 100  # 0b1100100
    print(f"Number of bit is: {count_bits(num)}")


if __name__ == "__main__":
    main()
