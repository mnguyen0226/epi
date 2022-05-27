from typing import List

from test_framework import generic_test

# 5/18/2022
def search_first_of_k(A: List[int], k: int) -> int:
    left = 0
    right = len(A) - 1
    result = 0
    while left <= right:
        # avoid overflow
        middle = left + (right - left) // 2

        if A[middle] < k:
            left = middle + 1

        elif A[middle] == k:
            # by this way you will save the result, not returning the middle
            result = middle
            right = middle - 1

            # # keep traverse till get first appearance
            # while middle != 0 and A[middle] == A[middle - 1]:
            #     middle = middle - 1
            # return middle

        elif A[middle] > k:
            right = middle - 1

    # return -1
    return result

    # T: O(logN)
    # S: O(1)


def search_first_of_k2(A: List[int], k: int) -> int:

    return 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k2
        )
    )
