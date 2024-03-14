import math
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right + 1):
            bit_cnt = bin(i).count('1')
            if bit_cnt < 2:
                continue
            elif bit_cnt == 2:
                cnt += 1
                continue
            elif bit_cnt % 2 == 0:
                continue
            sqrt_bit_cnt = math.floor(math.sqrt(bit_cnt))
            flg = True
            for j in range(3, sqrt_bit_cnt + 1, 2):
                if bit_cnt % j == 0:
                    flg = False
                    break
            if flg:
                cnt += 1
        return cnt
                


        