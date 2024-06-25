from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        while nums:
            i = nums.pop(0)
            target = -i

            left = 0
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]

                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                elif total == target:
                    result.append(sorted([i, nums[left], nums[right]]))
                    left += 1

        final_result = []
        while result:
            el = result.pop(0)
            if el not in final_result:
                final_result.append(el)

        return final_result


print(Solution().threeSum([-2, 0, 1, 1, 2]))
