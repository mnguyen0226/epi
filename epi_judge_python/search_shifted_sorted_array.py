from typing import List

from test_framework import generic_test

# 5/25/2022
# LeetCode: Search in Rotated Sorted Array
def search_smallest_linear_search(A: List[int]) -> int:
    L, R = 0, len(A) - 1

    # We know that the A[L] < A[R] if it is sorted
    while A[L] > A[R]:
        L = L + 1

    return L

    # T: O(n)
    # S: O(1)


def search_smallest(A: List[int]) -> int:
    L, R = 0, len(A) - 1

    while L < R:  # can't be equal since the value is distinct
        M = L + (R - L) // 2

        # if we are in the larger portion
        if A[M] > A[R]:
            L = M + 1

        # if we are in the smaller portion, we will move R gradually smaller
        else:
            R = M

    return L


# 6/11/2022
# Using binary search, return the INDEX, not value
def search_smallest2(A: List[int]) -> int:
    L, R = 0, len(A) - 1

    # keep track of the smallest value and index
    smallest_value = A[0]
    smallest_index = -1

    # apply binary search
    while L <= R:
        # if we are in sorted portion
        if A[L] < A[R]:
            # update the smallest value and index
            if A[L] <= smallest_value:
                smallest_value = A[L]
                smallest_index = L
            break

        # if not in sorted portion, then do binary search
        M = L + (R - L) // 2

        # update the smallest value
        if A[M] <= smallest_value:
            smallest_value = A[M]
            smallest_index = M

        if A[M] >= A[L]:
            L = M + 1
        else:
            R = M - 1

    return smallest_index


# T: O(logn)
# S: O(1)

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest2,
        )
    )
