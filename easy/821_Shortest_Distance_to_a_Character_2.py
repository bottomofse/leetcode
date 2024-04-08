class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [0] * len(s)
        idx = s.find(c)
        cnt = 0
        for i in range(idx, len(s), 1):
            cnt = 0 if s[i] == c else cnt + 1
            result[i] = cnt
        idx = s.rfind(c)
        cnt = 0
        for i in range(idx, -1, -1):
            cnt = 0 if s[i] == c else cnt + 1
            result[i] = cnt if result[i] == 0 else min(result[i], cnt)
        return result