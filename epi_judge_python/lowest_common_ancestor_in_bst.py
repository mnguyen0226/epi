import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# 6/3/2022
# The naive way is to store both path in 2 arrays then check when the are different
# For BT, we can do recursion to find 2 nodes then bubble up, if a node has both True, then it must be a a LCA
# 3 cases: - if node overlap, if both left and right noexist, if both left and right exist, if either one exist
def find_lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:

    # applying recursion for BT
    def lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
        if tree is None:
            return None

        # Question: What do we want to do at this node? if the node is overlap then return that node
        if tree.data == s.data or tree.data == b.data:
            return tree

        # check left and right
        left_subtree = lca(tree.left, s, b)
        right_subtree = lca(tree.right, s, b)

        # if there is none left and right then return None. Here root node does exist
        if left_subtree is None and right_subtree is None:
            return None

        # if both of them are found, then return the parent node
        if left_subtree and right_subtree:
            return tree

        # if one or another, then return single one
        if left_subtree and not right_subtree:
            return left_subtree

        return right_subtree

    return lca(tree, s, b)


# T: O(n) since we visit all the node
# S: O(h) since the call stack is proportional to the height of the tree

# this method only work for BST since the tree is sorted
def find_lca_optimized_for_bst(
    tree: BstNode, s: BstNode, b: BstNode
) -> Optional[BstNode]:
    curr_node = tree

    # here we are trying to get so that s/b < curr_node < b/s. Since we traverse downward, LCA is when we immediate reach this condition
    while curr_node:

        # if the current node is lesser than both nodes, then we move right
        if curr_node.data < s.data and curr_node.data < b.data:
            curr_node = curr_node.right

        # if the current node is greater than both nodes, then we move left
        elif curr_node.data > s.data and curr_node.data > b.data:
            curr_node = curr_node.lefte

        # if the node is one of the two values or the node is between
        else:
            return curr_node


# T: O(h) / O(logN) since we use only half of the tree everytime
# S: O(h) since the height of the call stack is proportional to the height of the tree


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(
            find_lca_optimized_for_bst,
            tree,
            must_find_node(tree, s),
            must_find_node(tree, b),
        )
    )
    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_in_bst.py",
            "lowest_common_ancestor_in_bst.tsv",
            lca_wrapper,
        )
    )
