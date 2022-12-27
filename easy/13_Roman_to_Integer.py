class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        before_char = ''
        convert_result = 0
        for i in s[::-1]:
            add_value = dic[i]
            if i == 'I' and before_char in list('VX'):
                convert_result -= 1
                before_char = i
                continue
            if i == 'X' and before_char in list('LC'):
                convert_result -= 10
                before_char = i
                continue
            if i == 'C' and before_char in list('DM'):
                convert_result -= 100
                before_char = i
                continue
            convert_result += add_value
            before_char = i
        return convert_result
