import collections
import functools
from turtle import right
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:

    Status = collections.namedtuple("Status", ("num_target_nodes", "ancestor"))

    # Returns an object consisting of an int and a node. The int field is 0,
    # 1, or 2 depending on how many of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.
    def lca_helper(tree, node0, node1):
        if tree is None:
            return Status(num_target_nodes=0, ancestor=None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result
        num_target_nodes = (
            left_result.num_target_nodes
            + right_result.num_target_nodes
            + (node0, node1).count(tree)
        )
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor

# 6/7/2022
def lca2(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    # if root not is None
    if tree is None:
        return None

    # if root node overlap with either node, then it must be LCA
    if tree.data == node0.data or tree.data == node1.data:
        return tree

    # check if the left and right subtree are overlap with the node0 or node1
    left_subtree = lca(tree.left, node0, node1)
    right_subtree = lca(tree.right, node0, node1)

    # if both left and right overlap with both child node then the current node is the LCA
    if left_subtree and right_subtree:
        return tree

    # if none of the child are found, then it must not be LCA
    if left_subtree is None and right_subtree is None:
        return None

    # if we found the left or the right, return accordingly:
    if left_subtree:
        return left_subtree

    return right_subtree

# T: O(n) since we visit all the node
# S: O(h) with h is the height of the tree which is proportional to the height of the call stack.

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
