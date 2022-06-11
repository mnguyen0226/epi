from cgitb import small
import itertools
from typing import Iterator, List
import heapq

from sympy import Min
from test_framework import generic_test

# 5/25/2022
# Why is this iterator?
# Solution 1:     return sorted(sequence) - T: O(nlogn) - merged sort
# Solution 2: Insertion Sort O(k.n)
# Solution 3: Heap Sort O(k.logn)
def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    results = []
    min_heap: List[int] = []

    # we need to add k+1 element, but first add k to the heap, we will make +1 automatically
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    # itertool keep track of iteration in the sequence
    for x in sequence:
        smallest_val = heapq.heappushpop(min_heap, x)
        results.append(smallest_val)

    # when sequence is finish iterate, we pop the rest of the heap
    while min_heap:
        smallest_val = heapq.heappop(min_heap)
        results.append(smallest_val)

    return results


# 6/2/2022
import heapq


def sort_approximately_sorted_array2(sequence: Iterator[int], k: int) -> List[int]:
    # k is the width, thus we first take k+1 nums in the heap
    min_heap = []
    result = []

    for num in itertools.islice(sequence, k + 1):
        heapq.heappush(min_heap, num)

    # iterate through the rest of sequence
    for num in sequence:
        smallest_num_in_heap = heapq.heappop(min_heap)
        result.append(smallest_num_in_heap)
        heapq.heappush(min_heap, num)

    # pop the rest of min heap out
    while len(min_heap) != 0:
        smallest_num_in_heap = heapq.heappop(min_heap)
        result.append(smallest_num_in_heap)

    return result


# T: O (nlogk) with n is the number of element in the array and k is the size of the heap
# S: O (logk) with k is the number of element stored in the heap

import heapq


def sort_approximately_sorted_array3(sequence: Iterator[int], k: int) -> List[int]:
    result = []
    min_heap = []

    # add the first k+1 number in the min heap
    for _ in range(k + 1):
        value = next(sequence, None)
        if value is not None:
            heapq.heappush(min_heap, value)

    # go through till the heap is empty
    while min_heap:
        # get the smallest number
        smallest_value = heapq.heappop(min_heap)
        result.append(smallest_value)

        # get the next number in the sequence
        next_value = next(sequence, None)

        # add the new number to the heap.
        if next_value is not None:
            heapq.heappush(min_heap, next_value)

    return result


# T: O(klogn) with k is the size of the heap, logn is the time to insert or remove from the heap
# S: O(k), except for result - O(n), with k is the size of the heap


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array3(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )
