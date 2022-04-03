from multiprocessing import dummy
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:

    # Creates a dummy head
    dummy_head = tail = ListNode()

    # Traverse element wise and append to the tail
    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

        # make sure to move the tail
        tail = tail.next

    # Append the rest of the linked list to the dummy list
    tail.next = L1 or L2

    return dummy_head.next  # why? because of the empy node
    # Time Complexity: O(n+m) since traverse through nodes worst case
    # Space Complexity: O(1) since we reused all the node


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
