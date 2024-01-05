# 17. Letter Combinations of a Phone Number
from typing import List


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
