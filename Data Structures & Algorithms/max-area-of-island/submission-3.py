class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        maxArea = 0

        def bfs(r, c):
            area = 1
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,-1],[0,1]]

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c)) 
                        area += 1
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r,c)
                    maxArea = max(area, maxArea)
        
        return maxArea
