from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 5/17/2022
# the idea is to compare "pairs of node"
def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(left_node: BinaryTreeNode, right_node: BinaryTreeNode) -> bool:
        # case 1: if there is only root node then true
        if not left_node and not right_node:
            return True

        # case 2: if there is left child and right child, then check the value with its sub-child pair value
        elif left_node and right_node:
            return (
                left_node.data == right_node.data
                and check_symmetric(left_node.left, right_node.right)
                and check_symmetric(left_node.right, right_node.left)
            )

        # 1 child without another child (False)
        return False

    # case 3: if there is no node (True) or if there is root node then we check symmetric
    return not tree or check_symmetric(tree.left, tree.right)

    # T: O(n) because we visit all node
    # S: O(h) becase the code only run when the tree is symmetric, the callstack is proportional to the tree height.


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
