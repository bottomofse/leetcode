class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {}
        for i in list('qwertyuiop'):
            first[i] = 1
        second = {}
        for i in list('asdfghjkl'):
            second[i] = 1
        third = {}
        for i in list('zxcvbnm'):
            third[i] = 1
        ret = []
        for j in words:
            flg = True
            for k in j:
                if k.lower() not in first:
                    flg = False
                    break
            if flg:
                ret.append(j)
                continue
            flg = True
            for k in j:
                if k.lower() not in second:
                    flg = False
                    break
            if flg:
                ret.append(j)
                continue
            flg = True
            for k in j:
                if k.lower() not in third:
                    flg = False
                    break
            if flg:
                ret.append(j)
                continue
        return ret
