from typing import List


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        return [self.findLongestPrefix(i, wordsContainer) for i in wordsQuery]

    def findLongestPrefix(self, word: str, wordsContainer: List[str]) -> int:
        maximal = -1
        maximal_index = None

        for i in range(len(wordsContainer)):
            maximal_index = maximal_index if maximal_index is not None else i
            el = wordsContainer[i]

            m = self.longestCommonPrefix(word, el)

            if m > maximal or (
                m == maximal and len(el) < len(wordsContainer[maximal_index])
            ):
                maximal = m
                maximal_index = i

        return maximal_index

    def longestCommonPrefix(self, s1: str, s2: str) -> int:
        i = 0

        l1 = len(s1)
        l2 = len(s2)

        while i < l1 and i < l2:
            if s1[l1 - i - 1] == s2[l2 - i - 1]:
                i += 1
            else:
                break

        return i


wordsContainer = ["abc", "bca", "cab", "abb", "bac"]
wordsQuery = [
    "a",
    "b",
    "c",
    "aa",
    "ab",
    "ac",
    "ba",
    "bb",
    "bc",
    "ca",
    "cb",
    "cc",
    "aaa",
    "aab",
    "aac",
    "aba",
    "abb",
    "abc",
    "aca",
    "acb",
    "acc",
    "baa",
    "bab",
    "bac",
    "bba",
    "bbb",
    "bbc",
    "bca",
    "bcb",
    "bcc",
    "caa",
    "cab",
    "cac",
    "cba",
    "cbb",
    "cbc",
    "cca",
    "ccb",
    "ccc",
]

print(Solution().stringIndices(wordsContainer, wordsQuery))
