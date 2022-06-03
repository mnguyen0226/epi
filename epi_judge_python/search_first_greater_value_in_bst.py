from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
import bintrees

# 6/3/2022
# keep popping smallest value till the value > k, then return the previous key
def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    if tree is None:
        return None

    arr = []

    # using inorder traversal
    def in_order_dfs(tree, arr):
        if tree is None:
            return None
        in_order_dfs(tree.left, arr)
        arr.append(tree)
        in_order_dfs(tree.right, arr)

        return arr

    # we know that the array is sorted
    arr = in_order_dfs(tree, arr)

    # linear search
    for num in arr:
        if num.data > k:
            return num

    return None

    # T: O(n) for linear search
    # S: O(n) for array


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_greater_value_in_bst.py",
            "search_first_greater_value_in_bst.tsv",
            find_first_greater_than_k_wrapper,
        )
    )
