from typing import List

from test_framework import generic_test

# 6/1/2022
# This is leetcode easy: https://www.youtube.com/watch?v=P1Ic85RarKY&t=466s&ab_channel=NeetCode
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    """
    A, B are list
    m is the number of elements in the array A
    n is the number of elements in the array B
    """
    last = m + n - 1
    pos_m = m - 1
    pos_n = n - 1

    # replace larger values in the back
    while pos_m >= 0 and pos_n >= 0:
        if A[pos_m] >= B[pos_n]:
            A[last] = A[pos_m]
            pos_m -= 1
        else:
            A[last] = B[pos_n]
            pos_n -= 1
        last -= 1

    # if there are still number in array B, just keep replacing. If there are still number in array A, it has been automatically replaced
    while pos_n >= 0:
        A[last] = B[pos_n]
        pos_n -= 1
        last -= 1


# T: O(n)
# S: O(1)


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )
