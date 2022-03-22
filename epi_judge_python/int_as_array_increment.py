from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):  # trace till the second to last number
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1  # next number in reverse

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

    # Time Complexity: O(n)
    # Space Complexity: O(1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one
        )
    )
