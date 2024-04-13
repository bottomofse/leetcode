class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flip_rev = [[1 ^ j for j in reversed(i)] for i in image]
        return flip_rev