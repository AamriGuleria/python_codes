import heapq
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[False]*m for _ in range(n)]
        min_heap = [(0, 0, 0)]
        while min_heap:
            efforts, i, j = heapq.heappop(min_heap)

            if i == n - 1 and j == m - 1:
                return efforts

            if visited[i][j]:
                continue

            visited[i][j] = True

            for dx, dy in directions:
                nx, ny = i + dx, j + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    diff = abs(heights[i][j] - heights[nx][ny])
                    new_effort = max(efforts, diff)
                    heapq.heappush(min_heap, (new_effort, nx, ny))
        return 0