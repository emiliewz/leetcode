# 923. 3Sum With Multiplicity
from collections import Counter
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        A = list(set(arr))
        A.sort()
        n, res = len(A), 0

        for i, u in enumerate(A):
            tar = target - u
            j, k = i, n - 1
            while j <= k:
                v, w = A[j], A[k]
                if v + w < tar:
                    j += 1
                elif v + w > tar:
                    k -= 1
                else:
                    a, b, c = count[u], count[v], count[w]
                    if i < j < k:
                        res += a * b * c
                    elif i == j < k:
                        res += (a * (a - 1)) // 2 * c
                    elif i < j == k:
                        res += a * (b * (b - 1)) // 2
                    else:
                        res += (a * (a - 1) * (a - 2)) // 6
                    j += 1
                    k -= 1

        return res % MOD
