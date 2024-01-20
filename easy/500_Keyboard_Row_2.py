class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {}
        for i in list('qwertyuiopQWERTYUIOP'):
            keyboard[i] = 1
        for i in list('asdfghjklASDFGHJKL'):
            keyboard[i] = 2
        for i in list('zxcvbnmZXCVBNM'):
            keyboard[i] = 3
        ret = []
        for i in words:
            flg = True
            row = keyboard[i[0]]
            for j in i:
                if row != keyboard[j]:
                    flg = False
                    break
            if flg:
                ret.append(i)
        return ret