from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1

        while nums[0] > nums[right]:
            right = right // 2

        while right < len(nums) - 1 and nums[right] <= nums[right + 1]:
            right += 1

        right += 1
        nums1 = nums[right:]
        nums2 = nums[:right]

        f1 = self.binary_search(nums1, target)
        f2 = self.binary_search(nums2, target)

        if f1 == -1 and f2 == -1:
            return -1
        elif f1 != -1:
            return f1 + right
        elif f2 != -1:
            return f2

    def binary_search(self, lst: List[int], target: int) -> int:
        left = 0
        right = len(lst) - 1

        while left <= right:
            middle = (left + right) // 2

            if lst[middle] < target:
                left = middle + 1

            elif lst[middle] > target:
                right = middle - 1

            else:
                return middle

        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
