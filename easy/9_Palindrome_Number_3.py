class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x > 0 and x % 10 == 0:
            return False

        a, b = x, 0
        while a > 0:
            b = b * 10 + a % 10
            a //= 10
        return x == b
