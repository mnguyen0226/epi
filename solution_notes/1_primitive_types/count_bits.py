# 3/13/2022
# Write a program that count number of bits in an int
# Solution: Go through each number of int, then shift the number to the right


def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1  # get the last bit
        x >>= 1
    return num_bits


if __name__ == "__main__":
    print(count_bits(12))
