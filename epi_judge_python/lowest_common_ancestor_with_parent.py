import functools
from multiprocessing import dummy
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 5/24/2022
def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node0 is None or node1 is None:
        return None

    # using set to store parents because of instant search time
    parents_storages = set()

    while node0:
        parents_storages.add(node0.data)
        node0 = node0.parent

    while node1:
        if node1.data in parents_storages:
            return node1
        parents_storages.add(node1.data)
        node1 = node1.parent

    return None

    # T: O(n): because we traverse through all nodes
    # S: O(n): because we use set to store all nodes


def lca_better(
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

    # T: O(n)
    # S: O(1)


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(
            lca_better, must_find_node(tree, node0), must_find_node(tree, node1)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_with_parent.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
