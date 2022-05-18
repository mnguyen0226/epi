import itertools
from typing import Iterator, List
import heapq
from test_framework import generic_test

# 5/18/2022
# Using the min-heap and sliding window
def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    min_heap = []

    # adds the first k elements into min-heap. Sort if there are fewer than k elements
    for x in itertools.islice(sequence, k):
        print(f"-----\n Testing: {x}")
        heapq.heappush(min_heap, x)

    result = []

    # for every new element, add it to the min_heap and extract the smallest
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )
