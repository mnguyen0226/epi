from array import array
from typing import List

from test_framework import generic_test

# 6/1/2022
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    setA = set(A)
    setB = set(B)
    hashmap = set()
    result = []

    for num in setA:
        hashmap.add(num)

    for num in setB:
        if num in hashmap:
            result.append(num)

    return sorted(result)


# T: O(nlogn) by using sorted
# S: O(n) because of using hashmap


def intersect_two_sorted_arrays_improved(A: List[int], B: List[int]) -> List[int]:
    result = []

    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if A[i] not in result:
                result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
            
    return result

# T: O(n+m) linear time worst case with m n are length of the two array
# S: O(n) because of using array

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intersect_sorted_arrays.py",
            "intersect_sorted_arrays.tsv",
            intersect_two_sorted_arrays_improved,
        )
    )
