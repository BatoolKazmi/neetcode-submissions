class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        visited = []

        def dfs(r, c):
            # out of range
            if r == ROWS or c == COLS:
                return false

            if board[r][c] == "X" or (r,c) in visited:
                board[r][c] == "X"
                return true
            
            if board[r][c] == "O":
                visited.append((r,c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        
        return board
                
        