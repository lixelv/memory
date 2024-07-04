from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    i = 0

    while i < len(nums):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        i += 1

    return nums


print(bubble_sort([4, 3, 8, 9, 5]))
