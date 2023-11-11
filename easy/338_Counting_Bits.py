class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            cnt = 0
            tmp = i
            while tmp > 0:
                cnt += tmp % 2
                tmp = tmp // 2
            result.append(cnt)
        return result
