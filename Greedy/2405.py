# 2405. Optimal Partition of String
class Solution:
    def partitionString(self, s: str) -> int:
        res, cur = 1, set()
        for c in s:
            if c not in cur:
                cur.add(c)
            else:
                cur.clear()
                cur.add(c)
                res += 1

        return res
