class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start, end = 0, 0
        result = []
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                end += 1
            else:
                result.append([start, end]) if end -start >= 2 else None
                start, end = i + 1, i + 1
        result.append([start, end]) if end -start >= 2 else None
        return result