# 3/9/2022
# Compute the parity of a single 64 bits words
# Time complexity = O(n)
# Space complexity = O(1)


def parity_check(num):
    # Count number of 1 in num
    num_bits = 0
    while num:
        num_bits += num & 1
        num >>= 1

    # Check if the num_bits is odd or even
    parity = 0
    if num_bits % 2 == 0:
        parity = 0
    else:
        parity = 1
    return parity


def main():
    num = 100  # expect parity = 1
    print(f"Parity is: {parity_check(num)}")


if __name__ == "__main__":
    main()
