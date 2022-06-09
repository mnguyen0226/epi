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


def plus_one2(A: List[int]) -> List[int]:
    # if the last number is not 9, then increment by 1 and return
    if A[-1] != 9:
        A[-1] += 1
        return A

    # if the last number is 9
    for i in reversed(range(len(A))):
        A[i] += 1

        # after adding if curr index is not first index
        if i != 0:
            # note that we are not guarantee to be 10, just the last number
            if A[i] == 10:
                A[i] = 0  # and continue
            else:
                break  # we done
        else:  # after adding if the curr index is the first index
            # note that we are not guarantee to be 10, just the last number
            if A[i] == 10:
                A[i] = 0
                A.insert(0, 1)  # positiion, value
            else:
                break  # we done

    return A

    # T: O(n) because we iterate through all elements in the array
    # S: O(1) because we did not use any additional ds for storing data


def plus_one3(A: List[int]) -> List[int]:
    remember_one = True

    # reverse traverse
    for i in reversed(range(len(A))):
        # if not the front number
        if i != 0:
            if A[i] != 9:
                A[i] += remember_one
                break
            elif A[i] == 9:
                A[i] = 0

        # if is front number
        elif i == 0:
            if A[i] != 9:
                A[i] += remember_one
                break
            elif A[i] == 9:
                A[i] = 0
                A.insert(0, 1)  # position, value
    return A


# T: O(n)
# S: O(1)

# 6/9/2022
def plus_one4(A: List[int]) -> List[int]:
    if len(A) == 0:
        return A

    for i in reversed(range(len(A))):

        # if this is not the last number
        if i != 0:
            if A[i] == 9:
                A[i] = 0
            elif A[i] != 9:
                A[i] += 1
                break
        # if this is the last number
        if i == 0:
            if A[i] == 9:
                A[i] = 0
                A.insert(0, 1)  # insert at position 0 value 1
            elif A[i] != 9:
                A[i] += 1

    return A


# T: O(n) because we traverse through all elements in the array
# S: O(1) because we manipulate the array's elements in the array

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one4
        )
    )
