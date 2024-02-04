# 952. Largest Component Size by Common Factor
from collections import Counter, defaultdict
from itertools import combinations
from math import sqrt
from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(i, j):
            p1, p2 = find(i), find(j)
            p[p1] = p2

        def get_prime_factor(n):
            for i in range(2, int(sqrt(n)) + 1):
                if not n % i:
                    return get_prime_factor(n // i) | set([i])
            return set([n])

        n = len(nums)
        p = list(range(n))
        a = defaultdict(list)
        for i, j in enumerate(nums):
            for prime in get_prime_factor(j):
                a[prime].append(i)

        for k in a:
            for i in range(1, len(a[k])):
                union(a[k][i], a[k][i - 1])

        return Counter([find(i) for i in range(n)]).most_common()[0][1]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return 0
            p[p2] = p1
            return 1

        def find(i):
            if i != p[i]:
                p[i] = find(p[i])
            return p[i]

        def primes_set(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return primes_set(n // i) | set([i])
            return set([n])

        n = len(nums)
        p = [i for i in range(n)]
        primes = defaultdict(list)

        for i, num in enumerate(nums):
            pr_set = primes_set(num)
            for q in pr_set:
                primes[q].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes) - 1):
                union(indexes[i], indexes[i + 1])

        return max(Counter([find(i) for i in range(n)]).values())


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                p[p2] = p1
                rank[p1] += rank[p2]
            else:
                p[p1] = p2
                rank[p2] += rank[p1]
            return True

        def find(i):
            if i != p[i]:
                p[i] = find(p[i])
            return p[i]

        def common(i, j):
            f, s = nums[i], nums[j]
            k = 2
            while k <= min(f, s):
                if f % k == 0 and s % k == 0:
                    return True
                k += 1
            return False

        n = len(nums)
        p, rank = [i for i in range(n)], [1] * n
        for i, j in combinations(range(n), 2):
            if common(i, j):
                union(i, j)
        return max(rank)
