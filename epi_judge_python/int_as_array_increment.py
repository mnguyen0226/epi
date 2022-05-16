from typing import List

from test_framework import generic_test

# 5/15/2022
def plus_one(A: List[int]) -> List[int]:
    # Check empty
    if len(A) == 0:
        return A
    
    # Traverse through the array backwards
    for i in reversed(range(len(A))):
        
        # if there is a 9: if last position or not last position
        if A[i] == 9:
            if i == 0:
                A[i] = 0 
                A.insert(0, 1)
                break
            A[i] = 0
            
        # if the current number if not 9, then we just increment the value by 1
        else:
            A[i] += 1
            break
    return A

    # T: O(n) because of using for loop
    # S: O(1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one
        )
    )
