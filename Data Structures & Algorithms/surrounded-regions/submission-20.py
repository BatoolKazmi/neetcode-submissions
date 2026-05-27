class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            # out of range
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] == "X" or (r,c) in visited:
                return
            
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
        