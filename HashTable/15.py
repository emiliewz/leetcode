# 15. 3Sum
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n - 1):
            l, h = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                return res
            while l < h:
                cur = nums[l] + nums[i] + nums[h]

                if cur > 0:
                    h -= 1
                elif cur < 0:
                    l += 1
                else:
                    res.add((nums[i], nums[l], nums[h]))
                    l += 1
                    h -= 1
                    while l < h and nums[l] == nums[l - 1]:
                        l += 1
                    while l < h and nums[h] == nums[h + 1]:
                        h -= 1

        return res
