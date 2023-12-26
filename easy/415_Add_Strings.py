class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_list = list(num1)
        num2_list = list(num2)
        carry = 0
        result = ''
        while num1_list or num2_list:
            a = int(num1_list.pop()) if num1_list else 0
            b = int(num2_list.pop()) if num2_list else 0
            result = str((a + b + carry) % 10) + result
            carry = 1 if a + b + carry >= 10 else 0
        if carry == 1:
            result = '1' +  result
        return result
