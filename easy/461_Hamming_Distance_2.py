class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit = x ^ y
        cnt = 0
        while bit > 0:
            cnt += bit & 1
            bit = bit // 2
        return cnt
