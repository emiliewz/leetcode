# 935. Knight Dialer
from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        neighbours = {
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
        MOD = 10**9 + 7
        a = [1] * 10
        for _ in range(n - 1):
            tmp = [0] * 10
            for i in range(10):
                for nei in neighbours[i]:
                    tmp[i] += a[nei] % MOD
            a = tmp

        return sum(a) % MOD


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        neighbors = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        a = [1] * 10

        for _ in range(n - 1):
            tmp = [0] * 10
            for i in range(10):
                for k in neighbors[i]:
                    tmp[k] = (tmp[k] + a[i]) % MOD
            a = tmp
        return sum(a) % MOD


class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [(1, 2), (1, -2), (2, 1), (2, -1)]
        MOD = 10**9 + 7

        @cache
        def dp(x, y, k):
            if x < 0 or x >= 4 or y < 0 or y >= 3 or (x == 3 and y != 1):
                return 0
            if k == 0:
                return 1

            res = 0
            for dx, dy in directions:
                res += dp(x + dx, y + dy, k - 1)
                res += dp(x - dx, y - dy, k - 1)
            return res % MOD

        res = 0
        for i in range(4):
            for j in range(3):
                res += dp(i, j, n - 1)
        return res % MOD


class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [
            (-1, -2),
            (-1, 2),
            (-2, -1),
            (-2, 1),
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
        ]

        @cache
        def dp(x, y, k):
            if x < 0 or x >= 4 or y < 0 or y >= 3 or (x == 3 and not y == 1):
                return 0
            if k == n - 1:
                return 1
            res = 0
            for dx, dy in directions:
                res += dp(x + dx, y + dy, k + 1)
            return res

        res = 0
        for i in range(4):
            for j in range(3):
                res += dp(i, j, 0)
                res %= 10**9 + 7

        return res


class Solution:
    def knightDialer(self, n: int) -> int:
        memo = {}

        directions = [
            (-1, -2),
            (-1, 2),
            (-2, -1),
            (-2, 1),
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
        ]

        def dp(x, y, k):
            if (x, y, k) in memo:
                return memo[(x, y, k)]
            if x < 0 or x >= 4 or y < 0 or y >= 3 or (x == 3 and not y == 1):
                return 0
            if k == n - 1:
                return 1

            res = 0
            for dx, dy in directions:
                res += dp(x + dx, y + dy, k + 1)

            memo[(x, y, k)] = res
            return res

        res = 0
        for i in range(4):
            for j in range(3):
                res += dp(i, j, 0)

        return res % (10**9 + 7)
