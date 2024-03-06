# 1542. Find Longest Awesome Substring
class Solution:
    def longestAwesome(self, s: str) -> int:
        digits = {str(i): 1 << int(i) for i in range(10)}
        res, mask = 0, 0
        a = {0: -1}
        for i, c in enumerate(s):
            mask ^= digits[c]
            for j in digits:
                cur = mask ^ digits[j]
                if cur in a:
                    res = max(res, i - a[cur])
            if mask in a:
                if res < i - a[mask]:
                    res = i - a[mask]
            else:
                a[mask] = i

        return res
