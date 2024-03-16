# 1616. Split Two Strings to Make Palindrome
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        l, r = 0, n - 1
        while l < r:
            if a[l] == b[r]:
                l += 1
                r -= 1
            else:
                break
        s1, s2 = a[l : r + 1], b[l : r + 1]
        l, r = 0, n - 1
        while l < r:
            if b[l] == a[r]:
                l += 1
                r -= 1
            else:
                break
        s3, s4 = a[l : r + 1], b[l : r + 1]
        return any(s == s[::-1] for s in (s1, s2, s3, s4))
