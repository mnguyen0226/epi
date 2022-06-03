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


# What about we don't need to store in array. We use
def find_first_greater_than_k_optimized(tree: BstNode, k: int) -> Optional[BstNode]:
    curr_node, smallest_larger_than_k = tree, None

    while curr_node:
        if curr_node.data > k:
            smallest_larger_than_k = curr_node
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

    return smallest_larger_than_k


# T: O(h) with h is the height of the tree, not n since we delete half the tree everytime
# S: O(1) since no data structure to store the data


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k_optimized(tree, k)
    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_greater_value_in_bst.py",
            "search_first_greater_value_in_bst.tsv",
            find_first_greater_than_k_wrapper,
        )
    )
