from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    flag = 1
    if (num1[0] < 0) ^ (num2[0] < 0):  # this need to be XOR
        flag = -1
    else:
        flag = 1

    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (
        len(num1) + len(num2)
    )  # the result will have less zeros than this initialized array

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]

            # get the last number of multiplication
            result[i + j] += (
                result[i + j + 1] // 10
            )  # floor division gets the front digit

            result[i + j + 1] %= 10  # mod give the remainder

    # Remove the leading zeros. Explain:
    # next((i for i, x in enumerate(result) if x != 0), len(result)) >> return the index of the first digit or the length of the result
    # thus the number will be result[first_none_zero : ]
    # however if the case of [0,0,....0] is return, we want to return [0] for addition

    # result = result[
    #     next((i for i, x in enumerate(result) if x != 0), len(result)) :
    # ] or [0]

    # return [flag * result[0]] + result[1:]

    # Get index of the next none-zero
    next_none_zero = next((i for i, x in enumerate(result) if x != 0), len(result))
    result = result[next_none_zero:]
    if result == []:  # since [0,0,....0] will be []
        result = [0]

    return [flag * result[0]] + result[1:]

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_multiply.py", "int_as_array_multiply.tsv", multiply
        )
    )
