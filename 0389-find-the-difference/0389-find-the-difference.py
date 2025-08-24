class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = defaultdict(int)

        for i in s:
            a[i] += 1
        
        for j in t:
            a[j] -= 1
        
        for c in a:
            if a[c]:
                return c
        

