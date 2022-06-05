from operator import ne
from turtle import back
from typing import List

from test_framework import generic_test

# 6/5/2022
# Apply backtracking via bruteforce


def n_queens(n: int) -> List[List[int]]:
    res = []
    board = []

    # hashmap to keep track
    col = set()
    pos_diag = set()  # r + c to be constant then it is in the same positive diagonal
    neg_diag = set()  # r - c to be constant then it is in the same negative diagonal

    def backtracking(r):
        if r == n:
            copy = (
                board.copy()
            )  # make a copy of board and append so when we escape the backtracking, it can remove
            res.append(copy)
            return

        # go through each column
        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # update the set and board before backtrack
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)

            # update the board: at the current row, what column are we adding a queen
            board.append(c)

            # backtrack recursion
            backtracking(r + 1)

            # un-update
            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board.remove(c)

    backtracking(0)

    return res


# T: O(N!) for the first queen we consider N position, for second qeen we consider N-2 position, ... then for N queen we got N! (not N^N)
# S: O(N^2) since we have N x N board if we don't consider the space for the output


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("n_queens.py", "n_queens.tsv", n_queens, comp))
