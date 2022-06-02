from typing import List

from test_framework import generic_test

# 6/1/2022
def smallest_nonconstructible_value(A: List[int]) -> int:
    A = sorted(A)
    # if you start with any coin larger than 1, then min nonconstructible value has to be 1
    smallest_sum = 1
    
    for num in A:
        # if the next number is way larger than the sum, meaning that the current smallest is the smallest non-constructible
        if smallest_sum < num:
            break
        
        # else all value to sum CAN be constructed so we keep adding to the sum - 1, we just add in the num
        smallest_sum += num

    return smallest_sum

# T: O(nlogn)
# S: O(1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "smallest_nonconstructible_value.py",
            "smallest_nonconstructible_value.tsv",
            smallest_nonconstructible_value,
        )
    )
