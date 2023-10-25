class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num2 = num
            num = 0
            while num2 > 0:
                num += (num2 % 10)
                num2 //= 10
        return num
