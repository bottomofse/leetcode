class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        field = [[0 for i in range(len(img[0]))] for j in range(len(img))]
        for  i in range(len(img)):
            for j in range(len(img[i])):
                cnt = 0
                sumval = 0
                for k in range(-1, 2, 1):
                    for l in range(-1, 2, 1):
                        if 0 <= i - k < len(img) and 0 <= j - l < len(img[0]):
                            cnt += 1
                            sumval += img[i - k][j - l]
                field[i][j] = sumval // cnt
        return field