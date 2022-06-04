import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

# 6/4/2022
# We will use recursion. Returning the calling stack
def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    moving_steps = []

    def recursive_hanoi(num_rings, moving_steps, peg_start, peg_end, peg_middle):
        if num_rings == 1:
            # move the ring from peg 1 to peg 3
            moving_steps.append([peg_start, peg_end])
        else:
            recursive_hanoi(num_rings - 1, moving_steps, peg_start, peg_middle, peg_end)
            moving_steps.append([peg_start, peg_end])
            recursive_hanoi(num_rings - 1, moving_steps, peg_middle, peg_end, peg_start)

        return moving_steps

    return recursive_hanoi(num_rings, moving_steps, 0, 2, 1)


# https://www.youtube.com/watch?v=VC4V67q2kEk&ab_channel=BasicsStrong
# T: O(2^n) since there are 2 recursive call per call, we got 2 > 2^2 > 2^3.....
# S: O(n) due to the call stack proprotional to the height of the tree, the height of the tree is equal to the number of disk


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure(
                "Illegal move from {} to {}".format(
                    pegs[from_peg][-1], pegs[to_peg][-1]
                )
            )
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "hanoi.py", "hanoi.tsv", compute_tower_hanoi_wrapper
        )
    )
