class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_list = list(pattern)
        s_list = list(s.split(' '))
        if len(pattern_list) != len(s_list):
            return False
        taiou1 = {}
        taiou2 = {}
        for i in range(len(pattern)):
            if pattern_list[i] not in taiou1:
                taiou1[pattern_list[i]] = s_list[i]
            if s_list[i] not in taiou2:
                taiou2[s_list[i]] = pattern_list[i]
            if taiou1[pattern_list[i]] != s_list[i] or taiou2[s_list[i]] != pattern_list[i]:
                return False
        return True