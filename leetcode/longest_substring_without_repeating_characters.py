class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximal = 0
        l = len(s)

        for c in range(len(s)):
            cache = set()
            i = c
            while True:
                el = s[i]
                if el in cache:
                    maximal = max(maximal, len(cache))
                    break
                else:
                    cache.add(el)
                    i += 1
                    if i == l:
                        maximal = max(maximal, len(cache))
                        break

        return maximal


print(Solution().lengthOfLongestSubstring("dvdf"))
