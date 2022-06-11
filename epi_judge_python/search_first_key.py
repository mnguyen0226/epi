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
    L, R = 0, len(A) - 1
    found = -1

    while L <= R:
        M = L + (R - L) / 2
        M = int(M)

        if A[M] < k:
            L = M + 1
        elif A[M] == k:
            found = M

            # the reason why we shift the right is due to we want the Middle to gradually go to the right to meet the first number. we will return the "found" index regardless
            R = M - 1
        else:
            R = M - 1

    return found


# T: O(logn) due to binary search
# S: O(1) due to not using any data structure to store space

# 6/11/2022
def search_first_of_k3(A: List[int], k: int) -> int:
    found = -1

    L, R = 0, len(A) - 1

    while L <= R:
        M = L + (R - L) // 2

        if A[M] < k:
            L = M + 1
        elif A[M] > k:
            R = M - 1
        else:
            found = M
            R = M - 1 
    return found

# T: O(logn) because we cut half of the number everytime
# S: O(1) since we use the elements in the array only

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k3
        )
    )
