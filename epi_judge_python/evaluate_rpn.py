from test_framework import generic_test


def evaluate(expression: str) -> int:
    # arr_exp = expression.split(",")
    # s = []
    # for i in range(len(arr_exp)):
    #     if (
    #         arr_exp[i] != '+'
    #         and arr_exp[i] != '-'
    #         and arr_exp[i] != '*'
    #         and arr_exp[i] != '/'
    #     ):
    #         s.append(int(arr_exp[i]))
    #     elif arr_exp[i] == "+":
    #         num2 = s.pop()
    #         num1 = s.pop()
    #         s.append(num1 + num2)
    #     elif arr_exp[i] == "-":
    #         num2 = s.pop()
    #         num1 = s.pop()
    #         s.append(num1 - num2)
    #     elif arr_exp[i] == "*":
    #         num2 = s.pop()
    #         num1 = s.pop()
    #         s.append(num1 * num2)
    #     elif arr_exp[i] == "/":
    #         num2 = s.pop()
    #         num1 = s.pop()
    #         s.append(int(num1 / num2))

    arr_exp = expression.split(",")
    s = []

    for c in arr_exp:
        if c == "+":
            s.append(s.pop() + s.pop())
        elif c == "-":
            a, b = s.pop(), s.pop()
            s.append(b - a)
        elif c == "*":
            s.append(s.pop() * s.pop())
        elif c == "/":
            a, b = s.pop(), s.pop()
            s.append(int(b / a))
        else:
            s.append(int(c))

    return s[0]

    # T: O(n) because we iterate through the array
    # S: O(1) because we don't use any additional data structure to store


def evaluate2(expression: str) -> int:
    arr_expression = expression.split(",")
    s = []

    for l in arr_expression:
        if l == "+":
            a, b = s.pop(), s.pop()
            s.append(a + b)
        elif l == "-":
            a, b = s.pop(), s.pop()
            s.append(b - a)
        elif l == "*":
            a, b = s.pop(), s.pop()
            s.append(a * b)
        elif l == "/":
            a, b = s.pop(), s.pop()
            s.append(b // a)
        else:
            s.append(int(l))

    return s[-1]


# T: O(n) with n is the expression in the string
# S: O(n) with n is the size of the stack


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate2)
    )
