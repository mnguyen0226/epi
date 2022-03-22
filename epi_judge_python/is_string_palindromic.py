from test_framework import generic_test


# 3/21/2022
def is_palindromic(s: str) -> bool:
    # reverse the string
    new_str = s[::-1]
    if s != new_str:
        return False
    return True

    # Space Compllexity: O(n)
    # Time Complexity: O(1) for 1 string


# Improvement On space complexity
# Note that arr[~i] for i in range(len(arr)) is arr[-(i+1)]
def is_palindromic_improved(s: str) -> bool:
    counter = 0
    for i in range(len(s) // 2):  # trace through half of the word
        if s[i] != s[~i]:
            counter += 1
    return True if counter == 0 else False

    # Space Complexity: O(1)
    # Time Complexity: O(1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic.py",
            "is_string_palindromic.tsv",
            is_palindromic_improved,
        )
    )
