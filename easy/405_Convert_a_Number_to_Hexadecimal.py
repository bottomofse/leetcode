class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num = 2 ** 32 + num
        henkan = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        ret = ''
        while num > 0:
            if num % 16 < 10:
                ret = str(num % 16) + ret
            else:
                ret = henkan[num % 16] + ret
            num = num // 16
        return ret        
