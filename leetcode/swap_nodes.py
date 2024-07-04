from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k = [int(i) for i in str(k)]

        i = -1
        while i >= -len(k) and i >= -len(num):
            s = num[i] + k[i]

            if s >= 10:
                s -= 10
                if -len(num) == i:
                    num.insert(0, 1)
                else:
                    num[i - 1] += 1

            num[i] = s
            i -= 1

        while num[i] == 10:
            num[i] = 0
            if -i == len(num):
                num.insert(0, 1)
            else:
                num[i - 1] += 1

            i -= 1

        return num


print(Solution().addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))
