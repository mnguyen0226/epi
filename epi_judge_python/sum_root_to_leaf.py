from curses import pair_content
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 5/24/2022
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def helper_sum(tree: BinaryTreeNode, partial_sum=0):
        # base case, if nothing then return 0
        if tree is None:
            return 0

        # here, there must be something, so we update the sum with current node data
        partial_sum = partial_sum * 2 + tree.data

        # check leave node
        if tree.left is None and tree.right is None:
            return partial_sum

        # if not leave node
        return helper_sum(tree.left, partial_sum) + helper_sum(tree.right, partial_sum)

    return helper_sum(tree)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", "sum_root_to_leaf.tsv", sum_root_to_leaf
        )
    )
