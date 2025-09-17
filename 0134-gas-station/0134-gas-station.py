class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        cur = 0
        idx = 0

        for i in range(n):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                idx = i+1
        
        return -1 if total < 0 else idx