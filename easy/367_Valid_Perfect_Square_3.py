class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 0
        right = num
        cnt = 0
        while left < right and cnt < 32:
            middle = (left + right) // 2
            if middle ** 2 == num:
                return middle
            elif middle ** 2 < num:
                left = middle
            else:
                right = middle
            cnt += 1
        return False
