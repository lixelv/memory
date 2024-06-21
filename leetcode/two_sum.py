from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while nums:
            current_element = nums.pop(0)
            i += 1

            sub_target = target - current_element

            if sub_target in nums:
                return [i - 1, nums.index(sub_target) + i]


print(two_sum([3, 2, 4], 6))
