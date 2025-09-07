class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, v in enumerate(citations):
            curCount = n-i
            if v >= n-i:
                return n-i
        
        return min(citations)



            #          1, 4, 7, 9, 10
            # idex.    0, 1, 2, 3, 4
            # curCount 5, 4, 3, 2, 1