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
    dummy_head.next = temp_L1 or temp_L2

    # skip the first node
    return new_list.next

    # T: O(n) for worst case that 1 list has the same length and has 12345.. altering
    # S: O(n) because we use an additional head node


def merge_two_sorted_lists2(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:

    dummy_head = tail = ListNode(0)

    L1_tail = L1
    L2_tail = L2

    while L1_tail and L2_tail:
        if L1_tail.data < L2_tail.data:
            tail.next = L1_tail
            L1_tail = L1_tail.next
            tail = tail.next
        else:
            tail.next = L2_tail
            L2_tail = L2_tail.next
            tail = tail.next

    if L1_tail:
        tail.next = L1_tail
    if L2_tail:
        tail.next = L2_tail

    return dummy_head.next


# T: O(n)
# S: O(1) because linked list don't take space and we reuse existing nodes


def merge_two_sorted_lists3(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:

    # create a dummy list
    dummy_head = tail = ListNode(0)

    # compare and attach accordingly
    while L1 and L2:
        if L1.data >= L2.data:
            tail.next = L2
            L2 = L2.next
        else:
            tail.next = L1
            L1 = L1.next
        tail = tail.next

    # attach the rest
    if L1:
        tail.next = L1
    if L2:
        tail.next = L2

    return dummy_head.next

# T: O(n) since we traverse two linked list
# S: O(1) because linked list don't take space and we reuse existing nodes

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists3
        )
    )
