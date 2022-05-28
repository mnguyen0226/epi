# 4/3/2022
# How to reverse a linked list iteratively using 2 pointers. Not sort
# This is the best solution.
def reverseListIter(head):
    prev, curr = None, head
    while curr:
        temp = curr.next  # temp wull be null
        curr.next = prev
        prev = curr  # last node
        curr = temp

    return prev
    # Time Complexity: O(n)
    # Space Complexity: O(1) cuz we use only the provided nodes


# How to reverse a linked list recursively
def reverseListRec(head):
    # base case: if the head is nulll
    if not head:
        return None

    newHead = head
    if head.next:  # is there is still more node
        newHead = reverseListRec(head.next)  # if this return something
        head.next.next = head

    head.next = None

    return newHead
    # Time Complexity: O(n)
    # Space Complexity: O(n)
