class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        m = 0

        for i,v in enumerate(nums):
            if i > m:
                return False

            if v+i >= n-1:
                return True

            if m < v+i:
                m = v+i

        return m >= n-1