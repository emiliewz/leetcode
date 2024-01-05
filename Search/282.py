# 282. Expression Add Operators
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(idx, total, last, expr):
            if idx == len(num):
                if total == target:
                    res.append(expr)
                    return

            for i in range(idx, len(num)):
                # if i > idx and num[idx] == "0":
                #     return
                s = num[idx : i + 1]
                n = int(s)
                if idx == 0:
                    backtrack(i + 1, n, n, str(n))
                else:
                    backtrack(i + 1, total - last + last * n, last * n, expr + "*" + s)
                    backtrack(i + 1, total + n, n, expr + "+" + s)
                    backtrack(i + 1, total - n, -n, expr + "-" + s)
                # if n == 0:
                #     return
                if i == idx and num[i] == "0":
                    return

        backtrack(0, 0, 0, "")
        return res
