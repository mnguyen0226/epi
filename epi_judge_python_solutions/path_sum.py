from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:

    if not tree:
        return False
    if not tree.left and not tree.right:  # Leaf.
        return remaining_weight == tree.data
    # Non-leaf.
    return has_path_sum(tree.left, remaining_weight - tree.data) or has_path_sum(
        tree.right, remaining_weight - tree.data
    )


def has_path_sum2(tree: BinaryTreeNode, remaining_weight: int) -> bool:

    def recursion(tree, remaining_weight):
        if tree is None:
            return False
        
        # there is a node, we update the remaining weight
        remaining_weight = remaining_weight - tree.data
    
        if remaining_weight == 0:
            return True
        
        return recursion(tree.left, remaining_weight) and recursion(tree.right, remaining_weight)
    
    return recursion(tree, remaining_weight)

# T: O(n) since we visit all the nodes in the worst case.
# S: O(h) with h is the height of the tree which is proportional to the height of the reccursion call stack.

if __name__ == "__main__":
    exit(generic_test.generic_test_main("path_sum.py", "path_sum.tsv", has_path_sum2))
