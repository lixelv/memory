class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [[] for _ in range(numRows)]

        i, d = 0, 1

        for j in s:
            print(i)
            result[i].append(j)

            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1

            i += d

        return "".join(["".join(i) for i in result])


print(Solution().convert("PAYPALISHIRING", 3))
