class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        cur = 0
        m = 0

        for i,v in enumerate(nums[:-1]):
            if m < i+v:
                m = i+v

            if i == cur:
                jumps += 1
                cur = m
            
        return jumps
