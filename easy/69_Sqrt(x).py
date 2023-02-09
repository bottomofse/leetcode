class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 2 ** 16 
        while left <= right:
            middle = (left + right) // 2
            if middle ** 2 == x:
                return middle
            if middle ** 2 < x and (middle + 1) ** 2 > x:
                return middle
            if middle ** 2 > x:
                right = middle
                continue
            if middle ** 2 < x:
                left = middle
                continue