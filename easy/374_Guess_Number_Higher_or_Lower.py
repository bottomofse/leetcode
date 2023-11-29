class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(0) == 0:
            return 0
        if guess(n) == 0:
            return n
        left = 0
        right = n
        while left < right:
            middle = (left + right) // 2
            res_guess = guess(middle)
            if res_guess == 0:
                return middle
            elif res_guess == 1:
                left = middle
            else:
                right = middle
