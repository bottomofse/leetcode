class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        img_x = len(image[0])
        img_y = len(image)        
        start_color = image[sr][sc]
        image[sr][sc] = color
        candidate = [[sc, sr]]
        if color == start_color:
            return image        
        while candidate:
            next_candidate = []
            for i in candidate:
                x = i[0]
                y = i[1]
                direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for j in direction:
                    d_x = j[0] + x
                    d_y = j[1] + y
                    if (0 <= d_x < img_x) and (0 <= d_y < img_y) and image[d_y][d_x] == start_color:
                        image[d_y][d_x] = color
                        next_candidate.append([d_x, d_y])
            candidate = next_candidate
        return image