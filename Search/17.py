# 17. Letter Combinations of a Phone Number
from functools import cache
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        a = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        n = len(digits)
        res = []

        @cache
        def dp(i, cur):
            if len(cur) == n:
                res.append(cur)
                return

            for j in range(i, n):
                for d in a[int(digits[j])]:
                    dp(j + 1, cur + d)

        dp(0, "")
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {}
        start = ord("a") - 2
        for i in range(2, 10):
            count = 3
            if i == 7 or i == 9:
                count = 4
            dict[str(i)] = []

            for j in range(count):
                dict[str(i)].append(chr(start + i + j))
            start = start + count - 1

        res = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in dict[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")
        return res


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # create letter dict
        dict = {}
        start = ord("a") - 2
        for i in range(2, 10):
            count = 3
            if i == 7 or i == 9:
                count = 4
            dict[str(i)] = []

            for j in range(count):
                dict[str(i)].append(chr(start + i + j))
            start = start + count - 1

        result = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            for c in dict[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return result
