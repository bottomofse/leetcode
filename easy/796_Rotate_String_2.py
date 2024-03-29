class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(s)
        for i in range(n):
            if s[0] == goal[i]:
                for j in range(n):
                    if s[j] != goal[(i + j) % n]:
                        break
                else:
                    return True
        return False