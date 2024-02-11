# 935. Knight Dialer
class Solution:
    def knightDialer(self, n: int) -> int:
        nei = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }
        a, MOD = [1] * 10, 10**9 + 7
        for _ in range(n - 1):
            tmp = [0] * 10
            for i in range(10):
                for j in nei[i]:
                    tmp[i] = (tmp[i] + a[j]) % MOD
            a = tmp

        return sum(a) % MOD
