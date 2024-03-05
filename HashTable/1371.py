# 1371. Find the Longest Substring Containing Vowels in Even Counts
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {}
        for i, v in enumerate(["a", "e", "i", "o", "u"]):
            vowels[v] = 1 << i
        a, mask, res = {}, 0, 0
        a[0] = -1

        for i, c in enumerate(s):
            if c in vowels:
                mask ^= vowels[c]
            if mask not in a:
                a[mask] = i
            else:
                res = max(res, i - a[mask])

        return res
