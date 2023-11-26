class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(2 ** 16):
            if i ** 2 == num:
                return True
        return False
