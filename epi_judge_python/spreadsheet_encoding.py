from test_framework import generic_test

# Helper function convert an int to string
def string_to_int(x: str) -> int:
    if x == "A":
        return 1
    elif x == "B":
        return 2
    elif x == "C":
        return 3
    elif x == "D":
        return 4
    elif x == "E":
        return 5
    elif x == "F":
        return 6
    elif x == "G":
        return 7
    elif x == "H":
        return 8
    elif x == "I":
        return 9
    elif x == "J":
        return 10
    elif x == "K":
        return 11
    elif x == "L":
        return 12
    elif x == "M":
        return 13
    elif x == "N":
        return 14
    elif x == "O":
        return 15
    elif x == "P":
        return 16
    elif x == "Q":
        return 17
    elif x == "R":
        return 18
    elif x == "S":
        return 19
    elif x == "T":
        return 20
    elif x == "U":
        return 21
    elif x == "V":
        return 22
    elif x == "W":
        return 23
    elif x == "X":
        return 24
    elif x == "Y":
        return 25
    elif x == "Z":
        return 26


# 3/27/2022
def ss_decode_col_id(col: str) -> int:
    # Get the base case
    if col == "":
        return 0

    res = 0
    power = 0

    # Go through each character with base 26 and convert to decimal with multiplication and addition
    for i in reversed(range(len(col))):
        digit = string_to_int(col[i])
        res += digit * pow(26, power)
        power += 1
    return res

    # Time Complexity: O(n) due to while loop
    # Space Complexity: O(1)


def ss_decode_col_id_improved(col: str) -> int:
    # Get the base case
    if col == "":
        return 0

    res = 0
    power = 0

    # Go through each character with base 26 and convert to decimal with multiplication and addition
    for i in reversed(range(len(col))):
        unicode = ord(col[i])  # get the unicode of A
        resize_unicode = unicode - 64  # resize A to have the value of 1
        digit = resize_unicode
        res += digit * pow(26, power)
        power += 1
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spreadsheet_encoding.py",
            "spreadsheet_encoding.tsv",
            ss_decode_col_id_improved,
        )
    )
