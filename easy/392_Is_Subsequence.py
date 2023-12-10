class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur = 0
        cnt = 0
        for i in s:
            while cur < len(t):
                if i == t[cur]:
                    cur += 1
                    cnt += 1
                    break
                cur += 1
        return cnt == len(s)
