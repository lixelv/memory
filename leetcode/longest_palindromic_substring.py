class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximal = 0
        maximal_string = ""
        l = len(s)

        for c in range(len(s)):
            i = c

            m, ms = self.expandCenter(s, i, i)
            if m > maximal:
                maximal = m
                maximal_string = ms

            m, ms = self.expandCenter(s, i, i + 1)
            if m > maximal:
                maximal = m
                maximal_string = ms

        return maximal_string

    def expandCenter(self, s, left, right):
        result = []

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if left != right:
                result.insert(0, s[left])
                result.append(s[right])
            else:
                result.insert(0, s[left])

            left -= 1
            right += 1

        return len(result), "".join(result)


print(Solution().longestPalindrome("babad"))
