import re


def round_to_32_bit(n):
    MIN_32_BIT = -(2**31)
    MAX_32_BIT = 2**31 - 1

    if n < MIN_32_BIT:
        return MIN_32_BIT
    elif n > MAX_32_BIT:
        return MAX_32_BIT
    else:
        return n


def bit32(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round_to_32_bit(result)

    return wrapper


class Solution:
    @bit32
    def myAtoi(self, s: str) -> int:
        s = re.sub(r"^(\s*)([\-\+]?)(0*)([1-9])", r"\2\4", s)

        re_str = r"^[\-\+]?\d+"
        number = re.findall(re_str, s)

        print(number)

        if number:
            return int(number[0])
        else:
            return 0


print(Solution().myAtoi("   -042"))
