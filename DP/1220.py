# 1220. Count Vowels Permutation
from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            a, e, i, o, u = e, (a + i) % MOD, (a + e + o + u) % MOD, (i + u) % MOD, a

        return (a + e + i + o + u) % MOD


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            a, e, i, o, u = (
                (e + i + u) % MOD,
                (a + i) % MOD,
                (e + o) % MOD,
                i,
                (i + o) % MOD,
            )

        return (a + e + i + o + u) % MOD


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            a_next = e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a

            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next

        return (a + e + i + o + u) % MOD


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        res = 0
        memo = {}

        def dp(i, cur):
            if (i, cur) in memo:
                return memo[(i, cur)]
            if i == n:
                return 1

            if cur == "a":
                memo[(i, cur)] = dp(i + 1, "e")
            elif cur == "e":
                memo[(i, cur)] = dp(i + 1, "a") + dp(i + 1, "i")
            elif cur == "i":
                memo[(i, cur)] = (
                    dp(i + 1, "a") + dp(i + 1, "e") + dp(i + 1, "o") + dp(i + 1, "u")
                )
            elif cur == "o":
                memo[(i, cur)] = dp(i + 1, "i") + dp(i + 1, "u")
            else:
                memo[(i, cur)] = dp(i + 1, "a")

            return memo[(i, cur)] % (10**9 + 7)

        for i in ["a", "e", "i", "o", "u"]:
            res += dp(1, i) % (10**9 + 7)

        return res % (10**9 + 7)


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        res = 0

        @cache
        def dp(i, cur):
            if i == n:
                return 1

            if cur == "a":
                return dp(i + 1, "e") % (10**9 + 7)
            if cur == "e":
                return (dp(i + 1, "a") + dp(i + 1, "i")) % (10**9 + 7)
            if cur == "i":
                return (
                    dp(i + 1, "a") + dp(i + 1, "e") + dp(i + 1, "o") + dp(i + 1, "u")
                ) % (10**9 + 7)
            if cur == "o":
                return (dp(i + 1, "i") + dp(i + 1, "u")) % (10**9 + 7)
            if cur == "u":
                return dp(i + 1, "a") % (10**9 + 7)

        for i in ["a", "e", "i", "o", "u"]:
            res += dp(1, i) % (10**9 + 7)
        return res % (10**9 + 7)
