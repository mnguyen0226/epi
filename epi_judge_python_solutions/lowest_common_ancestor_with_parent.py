import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))
    # Makes node0 as the deeper node in order to simplify the code.
    if depth1 > depth0:
        node0, node1 = node1, node0

    # Ascends from the deeper node.
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA.
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0

# 6/7/2022
def lca2(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    hashmap = set()
    
    # traverse from node0 to root
    while node0.parent:
        hashmap.add(node0.data)
        node0 = node0.parent
        
    # traverse from node1 to root and check hashmap
    while node1.parent:
        if node1.data in hashmap:
            return node1
        
        node1 = node1.parent
    
    return None

# T: O(n) with n is the max number of node from node0/node1 to root
# S: O(n) since we use hashmap

def lca2_optimize_space(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # iterate both node at the same time
    iter_node0 = node0
    iter_node1 = node1
    
    while iter_node0.data != iter_node1.data:
        # we did this first in case either start at the root
        if iter_node0 is None:
            iter_node0 = node1
        if iter_node1 is None:
            iter_node1 = node0
        
        # after they are valid, check for their values
        if iter_node1.data == iter_node0.data:
            return iter_node0
        
        # update the node
        node0 = node0.parent
        node1 = node1.parent
    
    return None
        
@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca2_optimize_space, must_find_node(tree, node0), must_find_node(tree, node1))
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
