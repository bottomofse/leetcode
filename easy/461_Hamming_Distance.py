class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit = x ^ y
        cnt = 0
        while bit > 0:
            cnt += 1 if bit % 2 != 0 else 0
            bit = bit // 2
        return cnt