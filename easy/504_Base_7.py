class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        code = True if num >= 0 else False
        if num < 0:
            num = -1 * num
        ret = ''
        while num > 0:
            ret = str(num % 7) + ret
            num = num // 7
        if code:
            return ret
        else:
            return '-' + ret
