from curses import def_prog_mode
from re import sub
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# 5/15/2022
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def dfs(root: BinaryTreeNode) -> list[bool, int]:
        # base case
        if not root:
            return [True, 0]

        left_check, right_check = dfs(root.left), dfs(root.right)
        balanced = (
            left_check[0]
            and right_check[0]
            and (abs(left_check[1] - right_check[1]) <= 1)
        )

        return [balanced, 1 + max(left_check[1], right_check[1])]

    return dfs(tree)[0]

    # T: O(n) because we visit all the node of the tree
    # S: O(h) we use recursion and the calll stack corresponds to a sequence of calls from the root throught the unique path the the current node, the stack height is therefore bounded by the height of tree


# 5/23/2022
def is_balanced_binary_tree2(tree: BinaryTreeNode) -> bool:
    def dfs_post_order(tree):
        # base case
        if tree is None:
            return (True, -1)

        # if not, then visit left subtree
        left_result = dfs_post_order(tree.left)
        # if any subtree is not balance we will return the value
        if not left_result[0]:
            return left_result

        # if not, then visit the right subtree
        right_result = dfs_post_order(tree.right)
        # if any subtree is not balance we will return the value
        if not right_result[0]:
            return right_result

        # calculate the height and balance status
        height = max(left_result[1], right_result[1]) + 1
        balance_status = abs(left_result[1] - right_result[1]) <= 1

        return (balance_status, height)

    return dfs_post_order(tree)[0]

    # T: O(n) because we visit all the node of the tree
    # S: O(h) we use recursion and the calll stack corresponds to a sequence of calls from the root throught the unique path the the current node, the stack height is therefore bounded by the height of tree


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
