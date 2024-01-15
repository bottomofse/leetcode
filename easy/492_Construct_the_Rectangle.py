import math
class Solution:
    def constructRectangle(self, c: int) -> List[int]:
        max_num = int(math.sqrt(c))
        for i in range(max_num, 0, -1):
            if c % i == 0:
                return [c // i, i]
