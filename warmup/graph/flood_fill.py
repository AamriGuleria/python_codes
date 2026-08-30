from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        while queue:
            i,j=queue.popleft()
            for dx,dy in directions:
                nx,ny = i+dx,j+dy
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == start_color:
                    image[nx][ny]=color
                    queue.append((nx,ny))
        image[sr][sc]=color
        return image