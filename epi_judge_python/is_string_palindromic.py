from test_framework import generic_test


# 5/15/2022
def is_palindromic(s: str) -> bool:
    # W1: simple cheat way
    # return s == s[::-1]

    # W2: check whether the first half of the string equal to the second half of the string
    return all(s[i] == s[~i] for i in range(len(s) // 2))
    
    # T: O(n)
    # S: O(1)
    
if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic.py",
            "is_string_palindromic.tsv",
            is_palindromic,
        )
    )
