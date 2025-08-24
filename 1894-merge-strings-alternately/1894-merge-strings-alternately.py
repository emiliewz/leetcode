class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        res = ''

        if n < m:
            for i in range(n):
                res += word1[i] 
                res += word2[i] 
            return res + word2[i+1:]
        elif n > m:
            for i in range(m):
                res += word1[i] 
                res += word2[i] 
            return res + word1[i+1:]
        else:
            for i in range(m):
                res += word1[i] 
                res += word2[i]
            return res
