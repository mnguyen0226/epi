from typing import List
import heapq
from test_framework import generic_test, test_utils

# 5/26/2022
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    max_heap: List[int] = []
    results = []
    
    for s in A:
        heapq.heappush(max_heap,-s)
    
    while k:
        max_num = -heapq.heappop(max_heap)
        results.append(max_num)
        k -= 1

    return results

# T: O(klogn) because of using priority queue. This is still better than nlogn + O(k) for merge sort and k extraction
# S: O(n) 

def k_largest_in_binary_heap2(A: List[int], k: int) -> List[int]:
    
    
    return []

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap2,
            comparator=test_utils.unordered_compare,
        )
    )
