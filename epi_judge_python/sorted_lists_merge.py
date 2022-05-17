from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# 5/16/2022
def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:
    new_list = ListNode()  # create empty list with a node 0
    dummy_head = new_list  # create dummy_head for traversal

    temp_L1 = L1  # get the first temp head node for traversal
    temp_L2 = L2  # get the second temp head node for traversal

    # we traverse and concatenate list altering
    while temp_L1 and temp_L2:
        if temp_L1.data < temp_L2.data:
            dummy_head.next = temp_L1
            temp_L1 = temp_L1.next
            dummy_head = dummy_head.next
        else:
            dummy_head.next = temp_L2
            temp_L2 = temp_L2.next
            dummy_head = dummy_head.next

    # concatenate if there is still value left
    if temp_L1:
        dummy_head.next = temp_L1

    if temp_L2:
        dummy_head.next = temp_L2

    # skip the first node
    return new_list.next

    # T: O(n) for worst case that 1 list has the same length and has 12345.. altering
    # S: O(n) because we use an additional head node


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
