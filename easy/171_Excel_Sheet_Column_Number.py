class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        num = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            result += (ord(columnTitle[i]) - 64) * num
            num *= 26
        return result