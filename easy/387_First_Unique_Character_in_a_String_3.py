class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char, cnt in Counter(s).items():
            if cnt == 1:
                return s.index(char)
        return -1
