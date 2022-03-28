from list_node import ListNode
from test_framework import generic_test

# 3/27/2022
# Giving a linked list head and the key, return the list node that contains the key
def search_list(L: ListNode, key: int) -> ListNode:
    # while the ListNode() is not null and we have not find the node that stores the key yet
    while L and L.data != key:
        L = L.next
    return L


def search_list_wrapper(L, key):
    result = search_list(L, key)
    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_in_list.py", "search_in_list.tsv", search_list_wrapper
        )
    )
