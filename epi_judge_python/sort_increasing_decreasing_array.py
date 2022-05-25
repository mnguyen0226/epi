from typing import List

from test_framework import generic_test

# 5/25/2022
def sort_k_increasing_decreasing_array_bf(A: List[int]) -> List[int]:

    return sorted(A)


# T: O(nlogn)
# S: O(1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_increasing_decreasing_array.py",
            "sort_increasing_decreasing_array.tsv",
            sort_k_increasing_decreasing_array_bf,
        )
    )
