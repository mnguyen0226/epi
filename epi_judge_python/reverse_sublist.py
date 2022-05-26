from multiprocessing import dummy
from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# 5/16/2022
def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    # get the head node of L
    dummy_head = sublist_head = ListNode(0, L)

    # traverse to prior sublist head
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # get the static iterator pointer
    sublist_iter = sublist_head.next

    # reverse linked list and keep count
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next,
            temp,
        )

    return dummy_head.next

    # T: O(n)
    # S: O(1) because we use exisiting node, not storing anything

def reverse_sublist2(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, L)
    
    for _ in range(1, start): # becuase the number starts with 1
        sublist_head = sublist_head.next
    
    sublist_iter = sublist_head.next
    
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    
    return dummy_head.next

    # T: O(n)
    # S: O(1) because we use exisiting node, not storing anything
    
if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist2
        )
    )
