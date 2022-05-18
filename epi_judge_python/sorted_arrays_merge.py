import enum
from typing import List, Tuple
import heapq

from test_framework import generic_test

# 5/18/2022 - brute-force
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # brute-force is to concate to an array and sorted it. This way does not use the fact that the sub-array is sorted
    arr = []

    for l in sorted_arrays:
        arr = arr + l

    return sorted(arr)  # O(nlogn)

    # T: O(nlogn) because using the sorted function
    # S: O(n)


# 5/18/2022 - Min-Heap
def merge_sorted_arrays2(sorted_arrays: List[List[int]]) -> List[int]:
    # create Min-Heap as a buffer. We want to store the value and the index of the k array
    min_heap: List[Tuple[int, int]] = []

    # create a list of iterators for each array in sorted_array
    sorted_arrays_iters = [
        iter(x) for x in sorted_arrays
    ]  # if there are 3 arrays there will be 3 iter

    # push the first (min) element to the min-heap. i is the index of the k array
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)  # get the value of the iteration
        if first_element is not None:
            # store the element and the index
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        # get the smallest value in the heap
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)

        # get the iterator off the smallest value in the heap
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]

        result.append(smallest_entry)

        # iterate to the new value
        next_element = next(smallest_array_iter, None)

        # update the min-heap with new value
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result

    # T: O(nlog(k)) because we use a heap to push and pop n elements in k arrays
    # S: O(k) because we use the min-heap to store 1 element of k array


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays2
        )
    )
