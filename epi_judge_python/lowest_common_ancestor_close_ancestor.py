import functools
from platform import node
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 5/31/2022
# https://www.youtube.com/watch?v=vZxxksAP8yk&ab_channel=CrackingFAANG
# one way is to store everynode in the path TO THE ROOT in a set and if meet again the return the node
def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    arr = set()

    while node0:
        arr.add(node0.data)
        node0 = node0.parent

    while node1:
        if node1.data in arr:
            return node1
        arr.add(node1.data)
        node1 = node1.parent

    return None

    # T: O(n) with h is the height of the tree
    # S: O(n) because we store the node in an array


def lca_hashmap(
    node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    # another way is to iterate the 2 node one by one and use the set to check if we already visit that node.
    # by iterate both node at the same time, we will have the time complexity proportion to the time that reach the headnode
    hashmap = set()

    while node0 or node1:
        # add data node0 and traverse
        if node0:
            if node0.data in hashmap:
                return node0
            hashmap.add(node0.data)
            node0 = node0.parent

        # add data node1 and traverse
        if node1:
            if node1.data in hashmap:
                return node1
            hashmap.add(node1.data)
            node1 = node1.parent

    return None

    # T: O(l) with l is the distance from child node to the LCA node
    # S: O(2l) -> O(l) with l is the number of node from child node to LCA node


# What is the way to use no-space? Using two pointers: one node move faster than another node.
# However, this way is not optimized for Time from node to LCA.
def lca_no_space_two_pointers(
    node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    n0 = node0
    n1 = node1

    while n0.data != n1.data:
        n0 = n0.parent
        if n0 is None:
            n0 = node1

        n1 = n1.parent
        if n1 is None:
            n1 = node0

    return n0


# S: O(1)
# T: O(h)


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(
            lca_no_space_two_pointers,
            must_find_node(tree, node0),
            must_find_node(tree, node1),
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
