from typing import List


class Solution:
    def binary(self, nums: List[int], target: int):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            el = nums[m][1]

            if el > target:
                r = m - 1
            elif el < target:
                l = m + 1
            else:
                return m
        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key=lambda x: x[1])

        while nums:
            el = nums.pop(0)
            sub_target = target - el[1]

            search = self.binary(nums, sub_target)

            if search != -1:
                return [el[0], nums[search][0]]


print(Solution().twoSum([3, 2, 4], 6))
