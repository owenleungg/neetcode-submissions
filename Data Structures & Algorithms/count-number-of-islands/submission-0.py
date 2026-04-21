class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    queue = deque([(r,c)])
                    seen.add((r,c))
                
                    while queue:
                        row, col = queue.popleft()
                        # check adjacent tiles
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr,nc) not in seen and grid[nr][nc] == "1":
                                seen.add((nr,nc))
                                queue.append((nr,nc))
                        
                    islands += 1
        
        return islands
                