class Solution:
    def isHappy(self, n: int) -> bool:
        loop_check = {}
        while True:
            next_n = 0
            for i in str(n):
                next_n += int(i) ** 2
            n = next_n
            if n in loop_check:
                return False
            if n == 1:
                return True
            loop_check[n] = 0
