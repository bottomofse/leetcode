class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for idx, character in enumerate(s):
            if count[character] == 1:
                return idx
        return -1
