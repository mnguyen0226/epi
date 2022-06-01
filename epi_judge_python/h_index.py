from re import sub
from typing import List

from test_framework import generic_test

# We need to sort it. Draw it out.
def h_index(citations: List[int]) -> int:
    citations = sorted(citations)
    n = len(citations)
    for i in range(len(citations)):
        if citations[i] >= n - i:
            return n - i

    return 0


# T: O(nlogn) due to sort
# S: O(1) since we use not data structure to store data


if __name__ == "__main__":
    exit(generic_test.generic_test_main("h_index.py", "h_index.tsv", h_index))
