from typing import List

from test_framework import generic_test, test_utils

# 6/5/2022
def permutations(A: List[int]) -> List[List[int]]:
    res = []

    if len(A) == 0:
        return res

    def backtracking(index: int, curr_A: List[int], rest_list: List[int]):
        if index == len(A):
            copy_A = curr_A.copy()
            res.append(copy_A)
            return

        for i in range(len(rest_list)):
            curr_A.append(rest_list[i])
            index += 1
            
            copy_rest_list = rest_list.copy() # this is for recovery
            rest_list = rest_list[:i] + rest_list[i + 1 :]

            backtracking(index, curr_A, rest_list)

            curr_A.pop()
            index -= 1
            rest_list = copy_rest_list

    backtracking(0, [], A)

    return res


# T: O(N!) due to permutation
# S: O(N) if the size of the output is not counted. Output size is equal to the size of the list

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "permutations.py",
            "permutations.tsv",
            permutations,
            test_utils.unordered_compare,
        )
    )
