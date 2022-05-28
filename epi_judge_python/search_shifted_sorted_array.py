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
    
    while L < R: # can't be equal since the value is distinct
        M = L + (R - L) // 2
        
        # if we are in the larger portion
        if A[M] > A[R]: 
            L = M + 1
            
        # if we are in the smaller portion, we will move R gradually smaller
        else:
            R = M
    
    return L

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )
