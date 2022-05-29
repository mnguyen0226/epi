from test_framework import generic_test

# 5/29/2022
def can_form_palindrome_self(s: str) -> bool:
    hashmap = {}
    more_than_one = False

    # put all character in a hashmap
    for c in s:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    # check the number of distinct character (appear only 1)
    more_than_one = sum([1 for x in hashmap if hashmap[x] == 1])

    # if there is non distinct character, we expect all character to be 2
    if more_than_one == 0:
        return all(True for x in hashmap if hashmap[x] == 2)

    # if there is 1 distinct character, we expect the rest character also to be 2
    elif more_than_one == 1:
        return all(True for x in hashmap if hashmap[x] <= 2)

    # if there are more than 2 distinct character, that is not palindrome
    return False


# T: O(n) because we go through all character in the string
# S: O(n) because we use hash table

# 5/29/2022
def can_form_palindrome(s: str) -> bool:
    hashmap = {}

    # put all character in a hashmap
    for c in s:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    # it is palindrome is the odd counted character appear only at most 1 time
    return sum([1 for x in hashmap if hashmap[x] % 2 == 1]) <= 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
