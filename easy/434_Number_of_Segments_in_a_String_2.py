class Solution:
    def countSegments(self, s: str) -> int:
        flg = True
        cnt = 0
        for i in list(s):
            if flg and i != ' ':
                cnt += 1
                flg = False
                continue
            if i == ' ':
                flg = True
                continue
        return cnt
