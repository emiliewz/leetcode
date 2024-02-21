# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = ""
        max_sub = 0
        for i, j in enumerate(s):
            if j not in cur:
                cur += j
                max_sub = max(max_sub, len(cur))
            else:
                idx = cur.index(j)
                cur = cur[idx + 1 :] + j
        return max_sub


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        l, max_sub = 0, 0
        for i, j in enumerate(s):
            if j in a:
                if a[j] < l:
                    max_sub = max(max_sub, i - l + 1)
                else:
                    l = a[j] + 1
            else:
                max_sub = max(max_sub, i - l + 1)
            a[j] = i
        return max_sub
