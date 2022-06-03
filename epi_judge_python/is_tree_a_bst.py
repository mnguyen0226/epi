from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import List

# 6/3/2022
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # idea is to visit the node in in-order traversal and see if the array is sorted in order
    if tree is None:
        return True

    arr_tree = []

    def in_order_traversal_iteration(tree: BinaryTreeNode):
        stack = []
        res = []

        # if the current node is not null or the stack is not empty
        while tree or stack:
            # keep go left
            while tree:
                stack.append(tree)
                tree = tree.left

            # append to the result
            tree = stack.pop()
            res.append(tree.data)

            # go right
            tree = tree.right

        return res

    def in_order_traversal_recursion(tree: BinaryTreeNode, arr_tree: List):
        # if there is nothing, then we return nothing
        if tree is None:
            return None

        # if there is something
        in_order_traversal_recursion(tree.left, arr_tree)
        arr_tree.append(tree.data)
        in_order_traversal_recursion(tree.right, arr_tree)

        # if there is something, we return the updated array, this line allow us to update the input array
        return arr_tree

    #    arr_tree = in_order_traversal_recursion(tree, arr_tree)
    arr_tree = in_order_traversal_iteration(tree)

    for i in range(0, len(arr_tree) - 1):
        if arr_tree[i] > arr_tree[i + 1]:
            return False

    return True


# T: O(h) with h is the height of the tree
# S: O(n) > O(h) since we use array to store the element, this is larger than the recursion call-stack


def is_binary_tree_bst_optmize(tree: BinaryTreeNode) -> bool:
    def DFS(tree: BinaryTreeNode, left_bound, right_bound):
        if tree is None:
            return True

        if not (tree.data <= right_bound and tree.data >= left_bound):
            return False

        return DFS(tree.right, tree.data, right_bound) and DFS(
            tree.left, left_bound, tree.data
        )

    return DFS(tree, float("-inf"), float("inf"))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_a_bst.py", "is_tree_a_bst.tsv", is_binary_tree_bst_optmize
        )
    )
