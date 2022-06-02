from cgitb import reset
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __lt__(self, other) -> bool:
        return (
            self.first_name < other.first_name
            if self.first_name != other.first_name
            else self.last_name < other.last_name
        )


# 6/1/2022
def eliminate_duplicate(A: List[Name]) -> None:
    # sort by first name
    A.sort(key=lambda name: name.first_name)

    i = 0  # iterator
    p = 0  # placeholder of distince value

    while i != len(A):
        if A[i].first_name != A[p].first_name:
            p += 1
            A[p] = A[i]
        i += 1

    # the ffu
    del A[p + 1 :]  # this is correct

    return


# T: O(nlogn) due to sort()
# S: O(1) since we did not use any additional data structure


@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "remove_duplicates.py",
            "remove_duplicates.tsv",
            eliminate_duplicate_wrapper,
            comp,
        )
    )
