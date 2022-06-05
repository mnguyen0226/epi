from turtle import back
from typing import List

from test_framework import generic_test, test_utils

# 6/4/2022
# Noted that the number range is [2-9]
# We need to use back-tracking, recursion, and a hashmap
def phone_mnemonic(phone_number: str) -> List[str]:
    if len(phone_number) == 0:
        return []

    hashmap = {
        "0": "0",
        "1": "1",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
    }

    # use global array
    res = []

    def backtracking(index: int, curr_string: str):
        # base case
        if len(curr_string) == len(phone_number):
            res.append(curr_string)
            return

        char_list = hashmap[phone_number[index]]
        for c in char_list:
            # note that don't update the current string here but update at the recursive time
            backtracking(index + 1, curr_string + c)

    backtracking(0, "")

    return res


# T: O(n*4^n) = length of each solution * number of solution
# S: O(n) if not counting for the length of the output. n is the length needed for the recursion stack


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            "phone_number_mnemonic.tsv",
            phone_mnemonic,
            comparator=test_utils.unordered_compare,
        )
    )
