class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = 2 ** 16
        while left < right:
            middle = (left + right) // 2
            sumcoin = (middle * (middle + 1)) // 2
            sumcoin2 = ((middle + 1) * (middle + 2)) // 2
            if sumcoin <= n and n < sumcoin2:
                return middle
            if sumcoin2 <= n:
                left = middle
                continue
            if sumcoin > n:
                right = middle
                continue
