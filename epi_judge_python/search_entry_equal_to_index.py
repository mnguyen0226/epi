import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 5/25/2022
# Using linear search
def search_entry_equal_to_its_index_linear_sort(A: List[int]) -> int:
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return -1


# T: O(n)
# S: O(1)


def search_entry_equal_to_its_index(A: List[int]) -> int:
    L, R = 0, len(A) - 1

    while L <= R:
        M = L + (R - L) // 2

        if A[M] < M:
            L = M + 1
        elif A[M] == M:
            return M
        else:
            R = M - 1

    return -1


# T: O(logn)
# S: O(1)


def search_entry_equal_to_its_index2(A: List[int]) -> int:
    L, R = 0, len(A) - 1
    found = -1
    while L <= R:
        M = L + (R - L) // 2

        if A[M] > M:
            R = M - 1
        elif A[M] < M:
            L = M + 1
        else:
            found = M
            break
    return found


# T: O(logn) due to binary search
# S: O(1)


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index2, A))
    if result != -1:
        if A[result] != result:
            raise TestFailure("Entry does not equal to its index")
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure("There are entries which equal to its index")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_entry_equal_to_index.py",
            "search_entry_equal_to_index.tsv",
            search_entry_equal_to_its_index_wrapper,
        )
    )
