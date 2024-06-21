from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        result = sum([customers[i] for i in range(len(customers)) if not grumpy[i]])
        combined = [(customers[i], i) for i in range(len(customers)) if grumpy[i]]
        maximal = 0

        for i in range(len(combined)):
            el, c_i = combined[i]
            sub_maximal = el

            j = i + 1
            while j < len(combined) and combined[j][1] - c_i >= minutes:
                sub_maximal += combined[j][0]

            maximal = max(maximal, sub_maximal)

        return result + maximal


print(Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
