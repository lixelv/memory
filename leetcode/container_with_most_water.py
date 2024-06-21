from typing import List


class Solution:
    def limit(self, num, limit):
        if num > limit:
            return limit
        else:
            return num

    def maxArea(self, height: List[int]) -> int:
        h = height
        enh = list(enumerate(h))
        left, right = 0, len(h) - 1

        while True:
            rl = (right, left)

            if h[left] > h[right]:
                for i, j in enh[left : right + 1]:
                    if j > h[right] and (i - left) * j > (right - left) * h[right]:
                        right = i
                        break

            if h[right] > h[left]:
                for i, j in enh[left : right + 1]:
                    if j > h[left] and (right - i) * j > (right - left) * h[left]:
                        left = i
                        break
            if rl == (right, left):
                break

        return min([h[left], h[right]]) * (right - left)


print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))
