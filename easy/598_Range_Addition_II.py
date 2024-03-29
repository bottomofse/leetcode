class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for i in ops:
            m = min(m, i[0])
            n = min(n, i[1])
        return m * n