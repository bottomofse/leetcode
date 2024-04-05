from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maximum = 0
        for c in combinations(points, 3):
            x = c[0]
            y = c[1]
            z = c[2]
            xy = [y[0] - x[0], y[1] - x[1]]
            xz = [z[0] - x[0], z[1] - x[1]]
            menseki = abs(xy[0] * xz[1] - xy[1] * xz[0]) / 2
            maximum = max(maximum, menseki)
        return maximum
