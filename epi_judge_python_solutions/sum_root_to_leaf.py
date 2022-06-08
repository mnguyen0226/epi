from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def sum_root_to_leaf_helper(tree, partial_path_sum=0):
        if not tree:
            return 0

        partial_path_sum = partial_path_sum * 2 + tree.data
        if not tree.left and not tree.right:  # Leaf.
            return partial_path_sum
        # Non-leaf.
        return sum_root_to_leaf_helper(
            tree.left, partial_path_sum
        ) + sum_root_to_leaf_helper(tree.right, partial_path_sum)

    return sum_root_to_leaf_helper(tree)


def sum_root_to_leaf2(tree: BinaryTreeNode) -> int:
            
    def recursionn_pre_order(tree: BinaryTreeNode, sum):
        if tree is None:
            return 0
        
        # there is something here, we then update the sum
        sum = sum * 2 + tree.data
        
        # if it is the only node, we will return that node as sum
        if tree.left is None and tree.right is None:
            return sum
        
        # if not, we will recursively update the sum accordinly to the left and right child
        return recursionn_pre_order(tree.left, sum) + recursionn_pre_order(tree.right, sum)

    return recursionn_pre_order(tree, 0)
    
# T: O(n) since we visit all the node
# S: O(h) with h is the height of the tree which is proportional to the recursion call stack

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", "sum_root_to_leaf.tsv", sum_root_to_leaf2
        )
    )
