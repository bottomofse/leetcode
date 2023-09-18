class Solution:
    def reverseBits(self, n: int) -> int:
        reverseStr = ''
        while n > 0:
            reverseStr = str(n % 2) + reverseStr
            n = n // 2
        reverseStr = ('0' * 32 + reverseStr)[-32:]
        result = 0
        #print(reverseStr)
        kisuu = 1
        for i in reverseStr:
            if i == '1':
                result += kisuu
            kisuu *= 2
        return result
