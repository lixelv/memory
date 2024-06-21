from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        maximal = 0
        for i in range(len(nums)):
            el = s.sub_rob(nums, i)
            if el > maximal:
                maximal = el

        return maximal

    def limit(self, n, low, high):
        if n < low:
            return low
        if n > high:
            return high
        else:
            return n

    def sub_rob(self, nums: List[int], index: int) -> int:
        el = nums[index]
        n = len(nums)

        nums = nums[: self.limit(index - 1, 0, n)] + nums[self.limit(index + 2, 0, n) :]
        n = len(nums)

        maximal = 0

        for i in range(n):
            sub_el = self.sub_rob(nums, i)
            if sub_el > maximal:
                maximal = sub_el

        return el + maximal


s = Solution()
nums = [1, 2, 3, 1]
print(s.rob(nums))
