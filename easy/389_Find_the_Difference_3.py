class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ret = 0
        for c in s:
            ret ^= ord(c)
        for c in t:
            ret ^= ord(c)
        return chr(ret)
