from typing import List


class Solution:
    def findMedian(self, nums: List[int]) -> float:
        l = len(nums)

        if l % 2 == 1:
            return float(nums[l // 2])
        else:
            return (nums[l // 2 - 1] + nums[l // 2]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return None


result = [0, 0, 1, 4, 4, 5, 6, 7, 9, 10, 14, 14, 16, 18, 26, 30, 50, 54, 60]
result1 = [[0, 1, 4, 5, 7, 9, 10, 14, 16], [0, 4, 6, 14, 18, 26, 30, 50, 54, 60]]

print(sorted(result))
print(sorted(result1))
print(
    Solution().findMedian(result),
    Solution().findMedian(result1[0]),
    Solution().findMedian(result1[1]),
)
