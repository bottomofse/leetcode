class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dic = {}
        for i in list(s):
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i] = 1
        for i in list(t):
            if i not in s_dic:
                return i
            if s_dic[i] >= 2:
                s_dic[i] -= 1
                continue
            if s_dic[i] == 1:
                s_dic.pop(i)
                continue
