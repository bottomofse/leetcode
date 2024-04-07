class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [0] * len(s)
        idx = s.find(c)
        cnt = 0
        for i in range(idx, len(s), 1):
            if s[i] == c:
                cnt = 0
                
            else:
                cnt += 1
            result[i] = cnt
        idx = s.rfind(c)
        print(idx)
        cnt = 0
        for i in range(idx, -1, -1):
            print(i)
            if s[i] == c:
                cnt = 0
            else:
                cnt += 1
            result[i] = cnt if result[i] == 0 else min(result[i], cnt)
        return result