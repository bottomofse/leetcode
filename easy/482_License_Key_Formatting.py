class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_list = reversed(list(s))
        cnt = 0
        retStr = ''
        
        for i in s_list:
            if i == '-':
                continue
            if cnt == k:
                cnt = 0
                retStr = '-' + retStr
            retStr = i.upper() + retStr
            cnt += 1
        return retStr
