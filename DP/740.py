# 740. Delete and Earn
from typing import Counter, List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = {}
        for n in nums:
            if n in a:
                a[n] += 1
            else:
                a[n] = 1

        keys = sorted(a.keys())
        f, s = 0, 0

        for i in range(keys[0], keys[-1] + 1):
            f, s = max(a.get(i, 0) * i + s, f), f

        return max(f, s)


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = Counter(nums)

        f, s = 0, 0
        for i in range(max(a.keys()), -1, -1):
            f, s = max(i * a[i] + s, f), f

        return f


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = Counter(nums)

        prev, cur = 0, 0
        for i in range(max(a.keys()) + 1):
            prev, cur = cur, max(i * a[i] + prev, cur)

        return cur


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        a = [0] * (nums[-1] + 1)
        for i in nums:
            a[i] += 1

        f, s = 0, 0
        for i in range(nums[-1], -1, -1):
            f, s = max(i * a[i] + s, f), f

        return f


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        a = {i: 0 for i in range(nums[-1] + 1)}
        for i in nums:
            a[i] += 1

        f, s = 0, 0
        for i in range(nums[-1], -1, -1):
            f, s = max(i * a[i] + s, f), f

        return f


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = max(nums) + 1
        freq = [0] * n
        for i in nums:
            freq[i] += i

        max_points = [0] * n
        max_points[1] = freq[1]

        for i in range(2, n):
            max_points[i] = max(max_points[i - 2] + freq[i], max_points[i - 1])

        return max_points[-1]


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = max(nums) + 1
        freq = [0] * n
        for i in nums:
            freq[i] += i

        dp = [0] * (n + 1)
        dp[-2] = freq[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 2] + freq[i], dp[i + 1])
        return dp[0]
