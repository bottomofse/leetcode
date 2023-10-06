class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(-31, 32, 1):
            if 2 ** i == n:
                return True
        return False
