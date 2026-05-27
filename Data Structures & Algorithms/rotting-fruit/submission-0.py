class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        time = 0

        def turnRotten(r,c):
            if (r in range(ROWS) or c in range(COLS) or (r,c) not in visit or grid[r][c] == 1):
                grid[r][c] = 2
                visit.add((r,c))
                q.append([r,c])      

        for r in ROWS:
            for c in COLS:
                if grid[r][c] == 2:
                    visit.add((r,c))
                    q.append([r,c])

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                turnRotten(r + 1, c)
                turnRotten(r - 1, c)
                turnRotten(r, c + 1)
                turnRotten(r, c - 1)
            
            time += 1
        
        return time if time else - 1

                
                
