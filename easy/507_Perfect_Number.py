import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sqrt_num = int(math.sqrt(num))
        sum_dividers = 0
        for i in range(1, sqrt_num + 1):
            if num % i == 0:
                if i != num:
                    sum_dividers += i
                if num // i != num:
                    sum_dividers += num // i
        return sum_dividers == num