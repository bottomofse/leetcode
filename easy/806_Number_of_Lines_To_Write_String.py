class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = 1
        col = 0
        for i in s:
            w = widths[ord(i) - 97]
            if col + w > 100:
                row += 1
                col = w
            else:
                col += w
        return [row, col]