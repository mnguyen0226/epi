from test_framework import generic_test
from test_framework.test_failure import TestFailure


# 5/29/2022
# We need hashmap, doubly linked list, LRU/MRU nodes
class Node:
    def __init__(self, isbn: int, price: int):
        self.isbn = isbn
        self.price = price
        self.next = self.prev = None


class LruCache:
    def __init__(self, capacity: int) -> None:
        self.hashmap = {}  # map the isbn to node
        self.cap = capacity
        self.right_mru = self.left_lru = Node(0, 0)

        # build a doubly linked list
        self.right_mru.prev, self.left_lru.next = self.left_lru, self.right_mru

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

        # T: O(1), S: O(1) because of pointer

    def add(self, node: Node):
        prev, nxt = self.right_mru.prev, self.right_mru
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

        # T: O(1), S: O(n) because of pointer and hashtable

    def lookup(self, isbn: int) -> int:
        """Given an ISBN, return the corresponding price; if the element is not present, return -1. If the ISBN is present, 
        update that entry to be the most recently use ISBN."""
        if isbn not in self.hashmap:
            return -1

        # if isbn present, update to mru and return price
        self.remove(self.hashmap[isbn])
        self.add(self.hashmap[isbn])

        return self.hashmap[isbn].price

        # T: O(1), S: O(n) because of pointer and hashtable

    def insert(self, isbn: int, price: int) -> None:
        """If an ISBN is already present, insert should not update the price, but should update that ISBN to be the most recently used entry. Check for capacity"""
        if isbn in self.hashmap:
            # update the position in linked list and return price
            self.remove(self.hashmap[isbn])
            self.add(self.hashmap[isbn])
        else:  # if not found then we will create a new node, insert to the hash map and linked list
            self.hashmap[isbn] = Node(isbn, price)
            self.add(self.hashmap[isbn])

        # check for capacity
        if len(self.hashmap) > self.cap:
            lru = self.left_lru.next
            self.remove(lru)
            del self.hashmap[lru.isbn]

        # T: O(1), S: O(n) because of pointer

    def erase(self, isbn: int) -> bool:
        """Remove the specific ISBN and corresponnding value from the case. Return Ture is the ISBN was present, otherwise, return false"""
        if isbn in self.hashmap:
            self.remove(self.hashmap[isbn])
            del self.hashmap[isbn]
            return True
        return False

        # T: O(1), S: O(n) because of pointer and hashtable


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != "LruCache":
        raise RuntimeError("Expected LruCache as first command")

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == "lookup":
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    "Lookup: expected " + str(cmd[2]) + ", got " + str(result)
                )
        elif cmd[0] == "insert":
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == "erase":
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    "Erase: expected " + str(cmd[2]) + ", got " + str(result)
                )
        else:
            raise RuntimeError("Unexpected command " + cmd[0])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lru_cache.py", "lru_cache.tsv", lru_cache_tester
        )
    )
