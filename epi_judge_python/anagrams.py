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


# 6/12/2022
# we convert a word into an array of distinct count.
# then I will use hashmap to map the array with the word
def find_anagrams2(dictionary: List[str]) -> List[List[str]]:
    hashmap = {}
    result = []

    for word in dictionary:
        # create a standard word_count
        word_count = [0 for _ in range(128)]

        # convert a word into an array of number
        for char in word:
            char_num = ord(char)  # return the unicode of character
            word_count[char_num] += 1

        # convert array to tuple since dictionary hashmap can only hash immutable object
        word_count = tuple(word_count)

        # populate the hashmap
        if word_count not in hashmap:
            # create an array
            hashmap[word_count] = [word]
        else:
            hashmap[word_count].append(word)

    # return only the values
    for key in hashmap:
        if len(hashmap[key]) > 1:
            result.append(hashmap[key])

    return result


# T: O(m.n) with m is the number words in dictionary[] and n is the average length of each words
# S: O(m.n) with m is the number words in dictionary[] and n is the average length of each words


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams2,
            comparator=test_utils.unordered_compare,
        )
    )
