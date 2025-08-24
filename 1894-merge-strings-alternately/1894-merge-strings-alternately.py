class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        res = ''

        for i in range(min(n,m)):
            res += word1[i] 
            res += word2[i] 
        return res + (word2[i+1:] if n < m else word1[i+1:])
        