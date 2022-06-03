from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


# 6/3/2022
# Apply post-order
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:

    res = []
    stack = []
    curr = tree

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        res.append(curr.data)
        if len(res) == k:
            break

        curr = curr.left

    return res


# T: O(h) with h is the height of the tree
# S: O(h) with h since the recursion stack has the height proportional to the tree


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py",
            "k_largest_values_in_bst.tsv",
            find_k_largest_in_bst,
            test_utils.unordered_compare,
        )
    )
