from typing import List
from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for i in range(1, len(nums)):
            if nums[i - 1]:
                if nums[i] <= nums[i - 1]:
                    result += nums[i - 1] - nums[i] + 1
                    nums[i] = nums[i - 1] + 1

        return result


print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]))
