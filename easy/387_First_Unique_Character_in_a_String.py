class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dic = {}
        for i in list(s):
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i] = 1
        for i in range(len(s)):
            if s_dic[s[i]] == 1:
                return i
        return -1
