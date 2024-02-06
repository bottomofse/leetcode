class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        cnt = 0
        ret = []
        row = []
        for i in mat:
            for j in i:
                row += [j]
                if cnt == c - 1:
                    ret += [row]
                    row = []
                    cnt = 0
                else:            
                    cnt += 1
        return ret