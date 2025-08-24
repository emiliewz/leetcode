class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n = len(word1)
        m = len(word2)
        res = ''
        
        while i < n and j < m:
            res += word1[i] 
            res += word2[j]
            i+=1
            j+=1
        
        res += word1[i:]
        res += word2[j:]

        return res