from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp_str = ''
        for i in list(licensePlate):
            if i.isalpha():
                lp_str += i.lower()
        ret = ' ' * 1001
        for i in words:
            c1 = Counter(lp_str)
            c2 = Counter(i)
            if (c1 == (c1 & c2)) and (len(i) < len(ret)):
                ret = i
        return ret