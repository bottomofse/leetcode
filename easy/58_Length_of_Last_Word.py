class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        cnt = 0
        for i in s:
            if i == ' ':
                cnt = 0
            else:
                cnt += 1
        return cnt