import re
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 5/24/2022
def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if tree is None:
        return False

    # update the remaining weight at the current node
    remaining_weight = remaining_weight - tree.data

    # if leaf node
    if tree.left is None and tree.right is None:
        if remaining_weight == 0:
            return True
        return False

    return has_path_sum(tree.left, remaining_weight) or has_path_sum(
        tree.right, remaining_weight
    )

    # T: O(n) because we traverse through all the tree.
    # S: O(h) becase the recursion call stack is proportional to the height of the tree.


if __name__ == "__main__":
    exit(generic_test.generic_test_main("path_sum.py", "path_sum.tsv", has_path_sum))
