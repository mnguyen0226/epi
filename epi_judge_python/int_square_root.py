from cmath import sqrt
from test_framework import generic_test

# 5/25/2022
def square_root(k: int) -> int:
    x = 0
    
    # create a do while loop
    while True:
        x += 1
        
        # if x ^ 2 exceed the k then we just return the previous value
        if x**2 > k:
            x -= 1
            break
        
    return x

# T: O(n)
# S: O(1)

def square_root2(k: int) -> int:
    L, R = 0, k
    
    while L <= R:
        M = L + (R-L) // 2
        
        if M**2 > k:
            R = M - 1
        else:
            L = M + 1
    return L-1

# T: O(logn)
# S: O(1)

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root2
        )
    )
