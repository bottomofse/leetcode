class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        for i in s:
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i] = 1
        for i in t:
            if i in s_dic:
                s_dic[i] -= 1
                if s_dic[i] <= 0:
                    s_dic.pop(i)
            else:
                return False
        if s_dic:
            return False
        else:
            return True  