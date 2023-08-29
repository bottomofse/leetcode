class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            tmp = []
            if i == 0:
                tmp = [1]
            if i == 1:
                tmp = [1,1]
            if i > 1:
                for i in range(len(result[-1]) - 1):
                    tmp.append(result[-1][i] + result[-1][i + 1])
                tmp = [1] + tmp + [1]
            result.append(tmp)
        return result
        