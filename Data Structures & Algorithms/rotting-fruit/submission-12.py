class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        time = 0

        def turnRotten(r,c):
           if (0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visit and grid[r][c] == 1):
                grid[r][c] = 2
                visit.add((r,c))
                q.append((r, c))
     

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    q.append((r, c))


        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                turnRotten(r + 1, c)
                turnRotten(r - 1, c)
                turnRotten(r, c + 1)
                turnRotten(r, c - 1)
           
            time += 1
            
        
        for row in grid:
            if 1 in row:
                return -1
        return time

                
                
