from asyncore import write
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# 5/15/2022
# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    # if the array is empty then return 0
    if A is None:
        return 0

    write_index = 0

    for i in range(1, len(A)):
        # write_index is where you store the previous unique value
        if A[write_index] != A[i]:

            # append the next new unique value
            A[write_index + 1] = A[i]
            write_index += 1

        # if the value is repeated then just keep move on, aka continue

    # return the len/number of unique value
    return write_index + 1

    # T: O(n) because of using for loop
    # S: O(1) because of not using any additional data structure


# 5/21/2/2022
def delete_duplicates2(A: List[int]) -> int:
    if len(A) < 2:
        return len(A)

    p = 0
    for i in range(len(A)):
        if A[i] != A[p]:
            p += 1
            A[p] = A[i]
        else:
            continue

    return p + 1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates2, A))
    return A[:idx]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_array_remove_dups.py",
            "sorted_array_remove_dups.tsv",
            delete_duplicates_wrapper,
        )
    )
