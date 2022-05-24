import functools
from platform import node
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 5/23/2022
# https://www.youtube.com/watch?v=13m9ZCB8gjw&ab_channel=TusharRoy-CodingMadeSimple
def lca(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    # if the root node is null then no LCA
    if tree is None:
        return None

    # if either found node is root then return root
    if tree.data == node0.data or tree.data == node1.data:
        return tree

    # find the left and right node
    left_node = lca(tree.left, node0, node1)
    right_node = lca(tree.right, node0, node1)

    # if both node is found then return root
    if left_node is not None and right_node is not None:
        return tree

    # if none found then return none
    if left_node is None and right_node is None:
        return None

    # if found only one node but not other, then the LCA must be the left or right node.
    if left_node != None:
        return left_node

    return right_node


# T: O(n)
# S: O(h) due to recursive calls proportional to tree height


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
