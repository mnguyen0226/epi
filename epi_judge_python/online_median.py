from typing import Iterator, List
import heapq
from test_framework import generic_test

# 5/25/2022
def online_median(sequence: Iterator[int]) -> List[float]:
    # two heaps, small(max heap), large(min heap). Heap should be equal size

    max_heap: List[int] = []  # storing the smaller half
    min_heap: List[int] = []  # storing the larger half
    results: List[float] = []

    # keep adding value to the max heap, if the length is larger than 1 then transfer max element to the min heap
    for x in sequence:
        heapq.heappush(max_heap, -x)  # max heap

        # check the element is in order: make sure all element in small is less than the large
        if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
            wrong_element = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, wrong_element)

        # check the size is even
        if len(max_heap) - len(min_heap) > 1:
            wrong_element = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, wrong_element)
        if len(min_heap) - len(max_heap) > 1:
            wrong_element = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -wrong_element)

        # calculate the median everytime
        if len(max_heap) > len(min_heap):
            results.append(-max_heap[0])
        elif len(min_heap) > len(max_heap):
            results.append(min_heap[0])
        else:
            results.append((-max_heap[0] + min_heap[0]) / 2.0)

    return results


# T: O(logn) due to the adding and extracting element from the heap
# S: O(n) due to using 2 heaps to store all element


# 6/11/2022
# Note that the median is a middle number of an array or and average
import heapq


def online_median2(sequence: Iterator[int]) -> List[float]:
    result = []
    min_heap = []
    max_heap = []

    for num in sequence:
        heapq.heappush(max_heap, -num)

        # check correct add
        if max_heap and min_heap and -max_heap[0] > min_heap[0]:
            wrong_added_value = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, wrong_added_value)

        # check for balance
        # len(max_heap) larger than len(min_heap) max 1
        if len(max_heap) - len(min_heap) > 1:
            wrong_place_value = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, wrong_place_value)
        # len(min_heap) can't be larger than len(max_heap)
        if len(min_heap) - len(max_heap) > 0:
            wrong_place_value = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -wrong_place_value)

        # calculate median
        if len(max_heap) > len(min_heap):
            result.append(-max_heap[0])
        elif len(max_heap) == len(min_heap):
            result.append((-max_heap[0] + min_heap[0]) / 2.0)

    return result


# T: O(nlogn) with n is the number of element in the sequence
# S: O(logn) with n is thee number of element in the sequence


def online_median_wrapper(sequence):
    return online_median2(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "online_median.py", "online_median.tsv", online_median_wrapper
        )
    )
