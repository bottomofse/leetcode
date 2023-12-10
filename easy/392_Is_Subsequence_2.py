class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ite = iter(t)
        return all(ch in ite for ch in s)
