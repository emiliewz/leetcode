class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)

        if n < 10:
            return []
            
        a = set()
        a.add(s[:10])
        res = set()

        for i in range(10,n):
            cur = s[i-9:i+1]
            if cur not in a:
                a.add(cur)
            elif cur not in res:
                res.add(cur)

        return list(res)
