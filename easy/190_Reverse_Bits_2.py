class Solution:
    def reverseBits(self, n: int) -> int:
        cnt, ans = 0, 0
        while cnt < 32:
            tmp = n & 1
            ans <<= 1
            ans += tmp
            n >>= 1
            cnt += 1
        return ans
