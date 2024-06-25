from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        return "".join(
            [i * j for i, j in sorted(d.items(), key=lambda x: x[1], reverse=True)]
        )


print(Solution().frequencySort("loveleetcode"))
