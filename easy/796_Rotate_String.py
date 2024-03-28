class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(s)
        for i in range(n):
            if s[0] == goal[i]:
                flg = True
                for j in range(n):
                    if s[j] != goal[(i + j) % n]:
                        flg = False
                if flg:
                    return True
        return False