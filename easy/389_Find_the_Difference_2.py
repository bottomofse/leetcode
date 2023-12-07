class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_cnt = Counter(list(s))
        t_cnt = Counter(list(t))
        for i in t_cnt - s_cnt:
            return i
