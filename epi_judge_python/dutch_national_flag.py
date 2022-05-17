import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# 5/13/2022
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    smaller = 0

    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1

    for j in reversed(range(len(A))):
        if A[j] > pivot:
            A[j], A[larger] = A[larger], A[j]
            larger -= 1
    return

    # T: O(n)
    # S: O(1)


# 3//15/2022
def dutch_flag_partition_1(pivot_index: int, A: List[int]) -> None:
    pivot_value = A[pivot_index]
    min, max = 0, len(A) - 1

    # first pass, shift all values less than pivot to the left
    for i in range(len(A)):
        if A[i] < pivot_value:
            A[min], A[i] = A[i], A[min]
            min += 1

    # second pass, shift all values greater than pivot to the right
    for j in reversed(range(len(A))):
        if A[j] > pivot_value:
            A[max], A[j] = A[j], A[max]
            max -= 1
    return


# 5/17/2022
def dutch_flag_partition_2(pivot_index: int, A: List[int]) -> None:
    s_index = 0
    l_index = len(A) - 1
    p = A[pivot_index]

    # first iteration - move all small value to the left of the pivot
    for i in range(len(A)):
        if A[i] < p:
            # swap
            A[s_index], A[i] = A[i], A[s_index]
            s_index += 1

    # second iteration - move all large value to the right of the pivot
    for j in reversed(range(len(A))):
        if A[j] > p:
            # swap
            A[l_index], A[j] = A[j], A[l_index]
            l_index -= 1

    return

    # T: O(n) because we loop through the array but not nested loop
    # S: O(1) because we did not use any additional ds for storing


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition_2, pivot_idx, A))

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
