# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return x
        if x <= 2:
            return 1

        l, h = 0, x // 2
        while l < h:
            mid = l + (h - l) // 2
            if mid**2 <= x:
                if (mid + 1) ** 2 > x:
                    return mid
                l = mid + 1
            else:
                h = mid - 1
        return l
