import itertools
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        calc = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def ways(s):
            if s.isdigit():
                return [int(s)]
            res = []
            for i in range(len(s)):
                if s[i] in "*-+":
                    res += [
                        calc[s[i]](x, y)
                        for x, y in itertools.product(ways(s[0:i]), ways(s[i + 1 :]))
                    ]
            return res

        return ways(expression)
