# 1220. Count Vowels Permutation
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        MOD = 10**9 + 7

        for _ in range(n - 1):
            a, e, i, o, u = e, (a + i) % MOD, (a + e + o + u) % MOD, (i + u) % MOD, a

        return (a + e + i + o + u) % MOD
