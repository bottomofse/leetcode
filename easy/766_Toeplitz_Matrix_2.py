class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        H = len(matrix)
        W = len(matrix[0])
        for i in range(H - 1, -1, -1):
            check = matrix[i][0]
            for j in range(0, W, 1):
                for k in range(0, H, 1):
                    if j != k:
                        continue
                    if i + k >= H:
                        continue
                    if matrix[i + k][j] != check:
                        #print('1回目k：{},j：{}'.format(k, j))
                        return False
        for i in range(0, W, 1):
            check = matrix[0][i]
            for j in range(0, W, 1):
                for k in range(0, H, 1):
                    if j != k:
                        continue
                    if i + j >= W:
                        continue
                    if matrix[k][i + j] != check:
                        #print('2回目k：{},j：{}'.format(k, j))
                        return False
        return True