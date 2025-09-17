class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        k = 0
        for i,c in enumerate(s):
            res[k] += c
            if i // (numRows-1) % 2:
                k -= 1
            else:
                k += 1
        return ''.join(res)