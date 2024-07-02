from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [i for i in nums if i > 0]
        nums.sort()

        if len(nums) == 0 or nums[0] != 1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1

        return nums[-1] + 1


print(Solution().firstMissingPositive([0, 2, 2, 1, 1]))
