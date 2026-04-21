class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_area = 0
        directions = [(1,0), (0,1), (0, -1), (-1, 0)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    queue = deque([(r,c)])
                    seen.add((r,c))
                    area = 1

                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr,nc) not in seen and grid[nr][nc] == 1:
                                queue.append((nr,nc))
                                seen.add((nr,nc))

                                area += 1
                        
                    max_area = max(max_area, area)
            
        return max_area