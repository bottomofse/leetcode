class Solution:
    def digit_to_hex_str(self, n):
        return str(hex(n))[2:]

    def toHex(self, num: int) -> str:
        ret = []
        if num < 0: num += 2 ** 32
        while num > 0:
            d = num % 16
            ret.append(self.digit_to_hex_str(d))
            num //= 16
        if len(ret) == 0: ret = ['0']
        return ''.join(ret[::-1])
