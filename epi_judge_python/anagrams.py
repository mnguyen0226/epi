from typing import List
from collections import defaultdict
from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)

    for word in dictionary:
        # there are 128 different values
        char_count = [0 for _ in range(128)]

        for c in word:
            char_index = ord(c)
            char_count[char_index] += 1

        hashmap[tuple(char_count)].append(word)

    # return only the anagram that has more than 2 values
    results = [l for l in hashmap.values() if len(l) > 1]

    return results

    # T: O(m.n) with m is numnber of words in dict and n is the average length of words
    # S: O(n) by using hashmap


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare,
        )
    )
