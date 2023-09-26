class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check = {}
        for i,v in enumerate(s):
            if v not in check:
                check[v] = t[i]
                continue
            if check[v] != t[i]:
                return False
        check = {}
        for i,v in enumerate(t):
            if v not in check:
                check[v] = s[i]
                continue
            if check[v] != s[i]:
                return False
        return True
