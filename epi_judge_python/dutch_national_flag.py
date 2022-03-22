import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# 3/14/2022
# Solution 1: Go through the
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    left_idx = 0
    right_idx = len(A) - 1
    pivot_value = A[pivot_index]

    # Gather all the smaller pivot value to the right
    for i in range(len(A)):
        if A[i] < pivot_value:
            A[left_idx], A[i] = A[i], A[left_idx]
            left_idx += 1

    # Gather all the larger pivot value to the left
    for i in reversed(range(len(A))):
        if A[i] > pivot_value:
            A[right_idx], A[i] = A[i], A[right_idx]
            right_idx -= 1

    return A

    # Time Complexity: O(n)
    # Space Complexity: O(1) since we don't use any additional storage ds


# 3/19/2022
def dutch_flag_partition_practice_1(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller = 0
    larger = len(A) - 1
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A

    # Time Complexity: O(n)
    # Space Complexity: O(1)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition_practice_1, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure("Not partitioned after {}th element".format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "dutch_national_flag.py",
            "dutch_national_flag.tsv",
            dutch_flag_partition_wrapper,
        )
    )
