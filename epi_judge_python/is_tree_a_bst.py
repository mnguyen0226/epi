from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import List

# 6/3/2022
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # idea is to visit the node in pre-order traversal and see if the array is sorted in order
    if tree is None:
        return True

    arr_tree = []

    def pre_order_traversal_recursion(tree: BinaryTreeNode, arr_tree: List):
        # if there is nothing, then we return nothing
        if tree is None:
            return None

        # if there is something
        pre_order_traversal_recursion(tree.left, arr_tree)
        arr_tree.append(tree.data)
        pre_order_traversal_recursion(tree.right, arr_tree)

        # if there is something, we return the updated array, this line allow us to update the input array
        return arr_tree

    arr_tree = pre_order_traversal_recursion(tree, arr_tree)

    for i in range(0, len(arr_tree) - 1):
        if arr_tree[i] > arr_tree[i + 1]:
            return False

    return True


# T: O(h) with h is the height of the tree
# S: O(n) > O(h) since we use array to store the element, this is larger than the recursion call-stack

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_a_bst.py", "is_tree_a_bst.tsv", is_binary_tree_bst
        )
    )
