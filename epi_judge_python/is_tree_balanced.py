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


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
