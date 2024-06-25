import operator
from typing import List


def xor(a, b):
    return (a or b) and not (a and b)


def floordiv(a, b):
    result = abs(a) // abs(b)

    if xor(a < 0, b < 0):
        return -result

    else:
        return result


operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": floordiv,
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        while tokens:
            el = tokens.pop(0)

            if el in operations.keys():
                stack.append(operations[el](stack.pop(-2), stack.pop(-1)))

            else:
                stack.append(int(el))

        return stack[0]


print(Solution().evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))
