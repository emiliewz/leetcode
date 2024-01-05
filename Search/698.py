# 698. Partition to K Equal Sum Subsets
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        target = sum(nums) // k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backtrack(idx, k, total):
            if k == 0:
                return True
            if total == target:
                return backtrack(0, k - 1, 0)

            for i in range(idx, len(nums)):
                if (
                    total + nums[i] > target
                    or used[i]
                    or (i > idx and nums[i] == nums[i - 1] and not used[i - 1])
                ):
                    continue
                used[i] = True
                if backtrack(i + 1, k, total + nums[i]):
                    return True
                used[i] = False
            return False

        return backtrack(0, k, 0)
