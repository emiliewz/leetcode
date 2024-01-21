# 842. Split Array into Fibonacci Sequence
from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res = []
        l = len(num)

        def dfs(i, cur):
            if i == l:
                if len(cur) > 2:
                    res.append(cur)
                    return True
                return False

            for j in range(i, min(l, i + 10)):
                s = num[i : j + 1]
                n = int(s)
                if n > 2**31:
                    return False
                if j > i and num[i] == "0":
                    break
                if len(cur) < 2 or n == cur[-1] + cur[-2]:
                    if dfs(j + 1, cur + [n]):
                        return True
            return False

        dfs(0, [])
        return res[0] if res else []


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res = []

        def backtrack(i):
            if i == len(num):
                return len(res) > 2
            for j in range(i, min(i + 10, len(num))):
                n = int(num[i : j + 1])
                if n > 2**31:
                    return False
                if len(res) < 2 or (res[-1] + res[-2] == n):
                    res.append(n)
                    if backtrack(j + 1):
                        return True
                    res.pop()
                if j == i and num[j] == "0":
                    return False
            return False

        backtrack(0)
        return res
