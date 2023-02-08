class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list = list(a)
        b_list = list(b)
        carry = 0
        answer = ''
        while a_list or b_list:
            a_tmp = int(a_list.pop()) if a_list else 0
            b_tmp = int(b_list.pop()) if b_list else 0
            tmp = a_tmp + b_tmp + carry
            if tmp <= 1:
                answer = str(tmp) + answer
                carry = 0
                continue
            if tmp == 2:
                carry = 1
                answer = '0' + answer
                continue
            if tmp == 3:
                carry = 1
                answer = '1' + answer
                continue
        if carry == 1:
            answer = '1' + answer
        return answer
