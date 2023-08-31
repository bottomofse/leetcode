class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            if i < 2:
                result.append(1)
            else:
                next_result = []
                for i in range(len(result) - 1):
                    next_result.append(result[i] + result[i + 1])
                result = [1] + next_result + [1]
        return result