class Solution:
    def findComplement(self, num: int) -> int:
        calc_result = 0
        cur = 1
        while num > 0:
            if num % 2 == 0:
                calc_result += cur
            num = num // 2
            cur *= 2
        return calc_result
