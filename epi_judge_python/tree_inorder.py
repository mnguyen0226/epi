from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# 5/24/2022
def inorder_traversal_recursion(tree: BinaryTreeNode) -> List[int]:
    def helper(tree: BinaryTreeNode, arr=[]) -> BinaryTreeNode:
        # base case
        if tree is None:
            return []

        # if there is a node then recursive call
        helper(tree.left, arr)
        arr.append(tree.data)
        helper(tree.right, arr)

        # return the updated array
        return arr

    arr = helper(tree)

    return arr


# T: O(n) due to traverse through all the node
# S: O(h) due to recursive call is proportional to the height of the tree

# 5/24/2022
def inorder_traversal_iterative(tree: BinaryTreeNode) -> List[int]:
    stack = []
    arr = []
    curr = tree

    while stack or curr:

        # keep moving left and add all the left child
        while curr:
            stack.append(curr)
            curr = curr.left

        # if reach the end node, we will pop the left node, add to the result, and pop the previous left node, and move to the right
        curr = stack.pop()  # move back the pointer to parents node
        arr.append(curr.data)
        curr = curr.right

    return arr


# T: O(n) because we traverse through all node
# S: O(n) due to using the stack


# 6/8/2022
# Apply the stack
def inorder_traversal_iterative2(tree: BinaryTreeNode) -> List[int]:
    stack = []
    results = []

    while stack or tree:

        # keep adding to the left
        while tree:
            stack.append(tree)
            tree = tree.left

        # pop and append to the result list
        tree = stack.pop()
        results.append(tree.data)

        # append the right node to stack
        tree = tree.right

    return results


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_inorder.py", "tree_inorder.tsv", inorder_traversal_iterative2
        )
    )
