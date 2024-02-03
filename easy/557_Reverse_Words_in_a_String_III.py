class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split(' ')
        ret = ''
        for i in s_split:
            ret += i[::-1] + ' '
        return ret.strip()