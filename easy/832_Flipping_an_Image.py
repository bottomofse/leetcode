class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flip_rev = []
        for i in image:
            t = []
            for j in i[::-1]:
                t.append(j ^ 1)
            flip_rev.append(t)
        return flip_rev