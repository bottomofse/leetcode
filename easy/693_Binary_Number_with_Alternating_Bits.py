class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        check = ~(n % 2)
        while n > 0:
            remainder = n % 2
            if not (check ^ remainder):
                return False
            check = remainder
            n = n //2
        return True
            