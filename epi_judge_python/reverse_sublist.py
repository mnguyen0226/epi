from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# 4/3/2022 - Medium
def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(
        0, L
    )  # you are making a copy of the linked list

    # Traverse till the position
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverse sublist
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next

    # Time Complexity: O(n) due to traversal.
    # Space Complexity: O(1) since we are reusing the node.


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
