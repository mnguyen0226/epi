import enum
from re import L
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
    min_heap: List[Tuple[int, int]] = []  # value and index

    # create a list of iterators for each array in sorted_array
    sorted_arrays_iters = [
        iter(x) for x in sorted_arrays
    ]  # if there are 3 arrays there will be 3 iter

    # push the first (min) element to the min-heap. i is the index of the k array
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it)  # get the value of the iteration
        if first_element is not None:
            # store the element and the index
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        # get the smallest value in the heap
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)

        # From the index of array's index, we can get the interator
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]

        result.append(smallest_entry)

        # iterate to the new valu
        next_element = next(smallest_array_iter, None)

        # update the min-heap with new value
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result

    # T: O(nlog(k)) because we use a heap to push and pop n elements in k arrays
    # S: O(k) because we use the min-heap to store 1 element of k array


# 5/25/2022
def merge_sorted_arrays_bf(sorted_arrays: List[List[int]]) -> List[int]:
    # Concatenate all list to 1 array and sorted

    result = []

    for l in sorted_arrays:
        result = result + l

    return sorted(result)

    # T: O(kn * klogn) which is slower than O(n). Sorted all elements in each array. The priority queue (min heap) will have O(logn) which is a bug improvement
    # S: O(n) because we use array to store elements in other array


# 5/25/2022
# Use min-heap as the buffer.
# The only thing that we really need to remember are: heapq.heappush(List, value) and heapq.heappop()
def merge_sorted_arrays3(sorted_arrays: List[List[int]]) -> List[int]:
    # make a priority queue (defined as a list storing tuple) storing the value of the first elements in array and the index of the array
    min_heap: List[Tuple[int, int]] = []
    results = []

    # make iterator for all array
    iter_array = []
    for arr in sorted_arrays:
        # initialize the iterator of the array and append to the iter array
        iter_array.append(iter(arr))

    # traverse through the iter_array, get the first elements and store them in the heap
    for i in range(len(iter_array)):
        first_element = next(iter_array[i], None)  # return when there is no more item
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    # Here, we have populated the min-heap. Traverse through the list and inserting the values in the heap
    while min_heap:
        smallest_element, smallest_array_index = heapq.heappop(min_heap)
        results.append(smallest_element)

        # from the index, we can get the iterator and update the iterator
        next_element = next(
            iter_array[smallest_array_index], None
        )  # None is return when there is no more item

        # update the min_heap
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_index))

    return results

    # T: O(kn * klogn) which is slower than O(n). Sorted all elements in each array. The priority queue (min heap) will have O(logn) which is a bug improvement
    # S: O(n) because we use array to store elements in other array


# 6/9/2022
import heapq


def merge_sorted_arrays_4(sorted_arrays: List[List[int]]) -> List[int]:
    result = []
    min_heap = []
    iter_list = []

    # create an iterator for each array
    for i in range(len(sorted_arrays)):
        iter_list.append(iter(sorted_arrays[i]))

    # append the first k values of the database, add the (values, iter, index oof sorted_arrays) for retrieval
    for i in range(len(iter_list)):
        first_value = next(iter_list[i], None)  # return None when there is nothing
        if first_value is not None:
            heapq.heappush(min_heap, (first_value, i))

    while min_heap:
        # pop the smallest values in the heap
        (smallest_value, smallest_value_iter_index) = heapq.heappop(min_heap)
        result.append(smallest_value)

        # get the next value of the current iterator
        next_smallest_value = next(iter_list[smallest_value_iter_index], None)

        if next_smallest_value is not None:
            heapq.heappush(min_heap, (next_smallest_value, smallest_value_iter_index))

    return result

    # T: O(kn * klogn) which is slower than O(n). Sorted all elements in each array. The priority queue (min heap) will have O(logn) which is a big improvement
    # S: O(n) because we use array to store elements in other array


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays_4
        )
    )
