# 410. Split Array Largest Sum
from functools import cache
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def can_split(target):
            count, total = 1, 0
            for n in nums:
                count += total + n > target
                total = total + n if total + n <= target else n
            return count <= k

        while l <= r:
            mid = l + (r - l) // 2
            if can_split(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        @cache
        def dp(i, k):
            if k == 1:
                return sums[n] - sums[i]
            if k == n - i:
                return max(nums[i:])

            min_sum = float("inf")
            for j in range(i + 1, n + 1):
                cur_max = max(sums[j] - sums[i], dp(j, k - 1))
                min_sum = min(min_sum, cur_max)
            return min_sum

        return dp(0, k)


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def canSplit(max_sum):
            cur_sum, count = 0, 0
            for n in nums:
                count += cur_sum + n > max_sum
                cur_sum = cur_sum + n if cur_sum + n <= max_sum else n
            return count + 1 <= k

        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def canSplit(largest):
            cur_sum = 0
            count = 0

            for n in nums:
                cur_sum += n
                if cur_sum > largest:
                    cur_sum = n
                    count += 1
            return count + 1 <= k

        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        sums = [0] * (N + 1)

        for i in range(1, N + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        def get_sum(i, j):
            return sums[j + 1] - sums[i]

        @cache
        def dp(i, n):
            if n == 1:
                return get_sum(i, N - 1)

            min_sum = float("inf")
            for j in range(i, N - n + 1):
                min_sum = min(max(get_sum(i, j), dp(j + 1, n - 1)), min_sum)
            return min_sum

        return dp(0, k)
