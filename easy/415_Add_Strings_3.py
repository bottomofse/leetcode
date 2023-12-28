from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ret = ''
        for a, b in zip_longest(reversed(list(num1)), reversed(list(num2))):
            a = a if a is not None else 0
            b = b if b is not None else 0
            t = int(a) + int(b) + carry
            ret = str(t % 10) + ret
            carry = 1 if t >= 10 else 0
        return ret if carry == 0 else ('1' + ret)
