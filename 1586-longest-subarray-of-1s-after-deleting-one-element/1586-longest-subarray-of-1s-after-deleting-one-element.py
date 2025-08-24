class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # count all numbers, start from the first non zero
        # once encounter 0, use a new variable to hold
        left = 0
        k = 1

        for right, num in enumerate(nums):
            if not num:
                k -= 1
            
            if k < 0:
                if not nums[left]:
                    k += 1
                left += 1

        return right - left