class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = 2 ** 32 + num
        return str(hex(num))[2:]
