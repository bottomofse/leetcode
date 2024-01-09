class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        
        for hight_idx in range(len(grid)):
            for width_idx in range(len(grid[0])):
                if grid[hight_idx][width_idx] == 0:
                    continue
                if hight_idx == 0:
                    perimeter += 1
                if hight_idx == len(grid) - 1:
                    perimeter += 1
                if width_idx == 0:
                    perimeter += 1
                if width_idx == len(grid[0]) - 1:
                    perimeter += 1
                if 0 < hight_idx and grid[hight_idx - 1][width_idx] == 0:
                    perimeter += 1
                if hight_idx < len(grid) - 1 and grid[hight_idx + 1][width_idx] == 0:
                    perimeter += 1
                if 0 < width_idx and grid[hight_idx][width_idx - 1] == 0:
                    perimeter += 1
                if width_idx < len(grid[0]) - 1 and grid[hight_idx][width_idx + 1] == 0:
                    perimeter += 1
        return perimeter