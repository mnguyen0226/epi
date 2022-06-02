from typing import List

from test_framework import generic_test

# 6/1/2022
# The idea is that assume we got an array with all values can be produce to SUM called SV. Of course, we can't produce SV + 1
# Says, we add U to SV.
# Case 1: U <= SV + 1, meaning that we can produce all values till SV + U (include SV + 1) but not SV + U + 1, thus SV + U + 1 is the SMALLEST NONCONSTRUCTIBLE VALUE
# Case 2: U > SV + 1, meaning that we can produce all value till SV only, even if we add SV + U, we can't product SV + 1, thus SV + 1 is the SMALLEST NONCONSTRUCTIBLE VALUE
def smallest_nonconstructible_value(A: List[int]) -> int:
    A = sorted(A)
    max_non_construct = 0

    for num in A:
        if max_non_construct + 1 < num:
            break

        max_non_construct += num

    return max_non_construct + 1


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
