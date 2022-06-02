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


# 5/23/2022
def is_symmetric2(tree: BinaryTreeNode) -> bool:

    # we write it like this so that we can recursively check right and left subtree
    def check_equivalent(lst: BinaryTreeNode, rst: BinaryTreeNode) -> bool:
        # if there is only rootnode
        if rst is None and lst is None:
            return True

        # if both left and right tree are there
        elif rst and lst:
            return (
                rst.data == lst.data
                and check_equivalent(rst.right, lst.left)
                and check_equivalent(rst.left, lst.right)
            )

        # else either one not there is False
        return False

    return tree is None or check_equivalent(tree.left, tree.right)

    # T: O(n) because we visit all node
    # S: O(h) becase the code only run when the tree is symmetric, the callstack is proportional to the tree height. Because we dp height traversal


def is_symmetric3(tree: BinaryTreeNode) -> bool:

    if tree is None:
        return True

    def check_symmetric(tree: BinaryTreeNode):
        # if there only root node
        if tree.left is None and tree.right is None:
            return (True, tree.data)  # balance status and value

        # visit the left
        left_balance, left_value = check_symmetric(tree.left)
        if left_balance is False:
            return False, left_value

        # visit the right
        right_balance, right_value = check_symmetric(tree.right)
        if right_balance is False:
            return False, right_value

        # at this point, we know that left tree and right tree are balance.
        # check current node balance by checking left right value and their subtree as well
        new_balance = (
            True
            if left_value == right_value
            and tree.left.right.data == tree.right.left.data
            and tree.left.left.data == tree.right.right.data
            else False
        )

        return new_balance, tree.data

    return check_symmetric(tree)[0]


# T: O(h) with h is the height of the tree
# S: O(n) since the recursion stack is proportion to the height of the tree

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric3
        )
    )
