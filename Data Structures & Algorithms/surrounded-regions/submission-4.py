class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        visited = []

        def dfs(r, c):
            # out of range
            if r == ROWS or c == COLS:
                return False

            if board[r][c] == "X" or (r,c) in visited:
                board[r][c] == "X"
                return True
            
            if board[r][c] == "O":
                visited.append((r,c))
                if dfs(r + 1, c) and dfs(r - 1, c) and dfs(r, c + 1) and dfs(r, c - 1):
                    board[r][c] == "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        
        return board
                
        