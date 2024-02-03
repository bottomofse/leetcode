class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_A = 0
        cnt_L = 0
        for i in range(len(s)):
            if s[i] == 'A':
                cnt_A += 1
            if s[i] == 'L':
                cnt_L += 1
            else:
                cnt_L = 0           
            if cnt_L >= 3 or cnt_A >= 2:
                return False
        return True