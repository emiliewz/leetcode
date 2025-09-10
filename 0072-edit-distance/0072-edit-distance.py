class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        a = [i for i in range(n+1)]

        for i in range(1, m+1):
            tmp = a[:]
            a[0] = i
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    a[j] = tmp[j-1]
                else:
                    a[j] = min(tmp[j], tmp[j-1], a[j-1]) + 1

        return a[-1]