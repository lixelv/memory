from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n - 1, 0, -1):
            current_el = nums[i]
            next_el = nums[i - 1]
            if next_el < current_el:
                nums[i:] = nums[n - 1 : i - 1 : -1]
                j = i
                while next_el >= nums[j]:
                    j += 1
                nums[i - 1] = nums[j]
                nums[j] = next_el
                return

        nums[0:] = nums[::-1]

    def getPermutation(self, n: int, k: int) -> str:
        result = list(range(1, n + 1))

        for _ in range(k - 1):
            self.nextPermutation(result)

        return "".join(result)


print(Solution().getPermutation(3, 3))
