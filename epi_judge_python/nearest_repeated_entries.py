from math import dist
from typing import List, Dict

from test_framework import generic_test

# 5/31/2022
def find_nearest_repetition(paragraph: List[str]) -> int:
    hashmap: Dict[str, int] = {}
    min_distance = float("inf")

    for i, word in enumerate(paragraph):
        if word in hashmap:
            # update min distance and latest index
            min_distance = min(min_distance, i - hashmap[word])
            hashmap[word] = i
        else:
            hashmap[word] = i

    # we find the min distance
    if min_distance != float("inf"):
        return min_distance

    # we did not find the min distance
    return -1

    # T: O(n) with n is the length of the array
    # S: O(d) with d is the number of distinct words in the array stored in hashmap


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "nearest_repeated_entries.py",
            "nearest_repeated_entries.tsv",
            find_nearest_repetition,
        )
    )
