from turtle import back
from typing import List

from test_framework import generic_test, test_utils

# 6/5/2022
# Instead of thinking as permutation like adding differnet number at the time,
# we can draw a tree where we add a number or don't add a number while traverse through the array
def generate_power_set(input_set: List[int]) -> List[List[int]]:
    res = []

    def backtracking(index, subset):  # index == 0, subset = []
        if index == len(input_set):
            # here although we did not add the character but the index has been iterated to the end
            res.append(subset.copy())
            return

        # decision to include nums[index]
        subset.append(input_set[index])
        backtracking(index + 1, subset)

        # decion not to include nums[index]
        subset.pop()
        backtracking(index + 1, subset)

    backtracking(0, [])

    return res


# T: O(n * 2^n) because we got 2^n subset and each has the length of n
# S: O(N) same isze as the input set if we don't include the size of the output array


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
