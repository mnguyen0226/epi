from test_framework import generic_test

# 5/29/2022
def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    # check for each character in letter_next, the number of appearance is not more than the one in the magazine
    # noted that the magazine's dictionary can have more distinct letter than the letter's dictionary

    # replace space
    letter_text = letter_text.replace(" ", "")
    magazine_text = magazine_text.replace(" ", "")

    # create hashmap
    hashmap_letter = {}
    hashmap_magazine = {}

    # store character in hashmap
    for c in letter_text:
        if c not in hashmap_letter:
            hashmap_letter[c] = 1
        else:
            hashmap_letter[c] += 1

    # store character in hashmap
    for c in magazine_text:
        if c not in hashmap_magazine:
            hashmap_magazine[c] = 1
        else:
            hashmap_magazine[c] += 1

    # go through each hashmap
    for _ in range(len(hashmap_letter)):
        # get the character, counter
        char_letter, count_char_letter = hashmap_letter.popitem()

        # if there is not character in the magazine hashmap
        if char_letter not in hashmap_magazine:
            return False

        count_char_magazine = hashmap_magazine.get(char_letter)

        # if the letter character counter > magain character counter, this will be wrong
        if count_char_letter > count_char_magazine:
            return False

    return True


# T: O(n) because we traverse through character in string
# S: O(1) because we use hashmap

# Another way to do is use a single hash table and start deleting
def is_letter_constructible_from_magazine2(
    letter_text: str, magazine_text: str
) -> bool:

    # replace space
    letter_text = letter_text.replace(" ", "")
    magazine_text = magazine_text.replace(" ", "")

    hashmap = {}

    # store character in hashmap
    for c in letter_text:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    # go throught the magazine
    for c in magazine_text:
        if c in hashmap:
            hashmap[c] -= 1
        else:
            continue

    arr = []

    # go through the hashmap annd get char, count pair
    for _ in range(len(hashmap)):
        char, count = hashmap.popitem()

        # negative means over use
        if count <= 0:
            arr.append(True)
        else:
            arr.append(False)

    return all(arr)


# T: O(n) because we traverse through character in string
# S: O(1) because we use hashmap

# 6/11/2022
# Store both the letters and the magazine to the hashmap. Then compare the hashmap
def is_letter_constructible_from_magazine3(
    letter_text: str, magazine_text: str
) -> bool:

    hashmap_letter = {}
    hashmap_magazine = {}

    # remove whitespace in character and magazine
    letter_text = letter_text.replace(" ", "")
    magazine_text = magazine_text.replace(" ", "")

    # store character in letter
    for char in letter_text:
        if char not in hashmap_letter:
            hashmap_letter[char] = 0
        else:
            hashmap_letter[char] += 1

    # store character in magazine
    for char in magazine_text:
        if char not in hashmap_magazine:
            hashmap_magazine[char] = 0
        else:
            hashmap_magazine[char] += 1

    # compare the hashmap
    if len(hashmap_magazine) < len(hashmap_letter):
        return False

    # compare the key and the value of the key
    for key in hashmap_letter:
        if key not in hashmap_magazine:
            return False
        if hashmap_letter[key] > hashmap_magazine[key]:
            return False

    return True


# T: O(n) with n is the average length of the magazine
# S: O(n) with n is the length of the hashmap

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine3,
        )
    )
