import math
class Solution:
    memo = {}
    def countPrimeSetBits(self, left: int, right: int) -> int:
        sum_prime = 0
        for i in range(left, right + 1, 1):
            if self.is_prime_number(self.count_bin_bit(i)):
                sum_prime += 1
        return sum_prime

    def count_bin_bit(self, num: int) -> int:
        cnt = 0
        while num:
            if num % 2 == 1:
                cnt += 1
            num = num // 2
        return cnt

    def is_prime_number(self, num: int) -> bool:
        if num in self.memo:
            return True
        if num < 2:
            return False
        if num == 2:
            self.memo[num] = True
            return True
        if num % 2 == 0:
            return False
        sqrt_num = math.floor(math.sqrt(num))
        for i in range(3, sqrt_num + 1, 2):
            if num % i == 0:
                return False
        self.memo[num] = True
        return True