from test_framework import generic_test
from test_framework.test_failure import TestFailure

# # 5/17/2022
# class Stack:
#     def __init__(self):
#         self.s = []

#     def empty(self) -> bool:
#         # check the length
#         return len(self.s) == 0

#         # T: O(1)
#         # S: O(1)

#     def max(self) -> int:
#         max = self.s[0]
#         for i in range(len(self.s)):
#             if self.s[i] > max:
#                 max = self.s[i]
#         return max

#         # T: O(n)
#         # S: O(1)

#     def pop(self) -> int:
#         last_val = self.s[-1]

#         # slicing
#         self.s = self.s[:-1]
#         return last_val

#         # T: O(1)
#         # S: O(1)

#     def push(self, x: int) -> None:
#         self.s.append(x)
#         return

#         # T: O(1)
#         # S: O(1)

# 6/2/2022
class Stack:
    def __init__(self):
        """Constructor"""
        self.s = []
        self.max_s = []  # keep track of the max stack

        # T: O(1)
        # S: O(n)

    def empty(self) -> bool:
        # return if the len is empty
        return len(self.s) == 0

        # T: O(1)
        # S: O(1)

    def max(self) -> int:
        return self.max_s[-1]

        # T: O(1)
        # S: O(1)

    def pop(self) -> int:
        val = self.s[-1]
        del self.s[-1]
        del self.max_s[-1]
        return val

        # T: O(1)
        # S: O(1)

    def push(self, x: int) -> None:
        self.s.append(x)
        if len(self.max_s) == 0:
            self.max_s.append(x)
        else:  # compare with the largest one
            old_max = self.max_s[-1]
            if x > old_max:
                self.max_s.append(x)
            else:
                self.max_s.append(old_max)

        # T: O(1)
        # S: O(1)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
