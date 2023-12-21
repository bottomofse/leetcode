from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        cnt_palind = 0
        kisuu = False
        for i in count:
            if count[i] % 2 == 0:
                cnt_palind += count[i]
            else:
                cnt_palind += (count[i] // 2) * 2
                kisuu = True
        if kisuu:
            cnt_palind += 1
        return cnt_palind
