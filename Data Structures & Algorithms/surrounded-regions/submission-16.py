class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            # out of range
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return False

            # when an element is X remain X
            if board[r][c] == "X" or (r,c) in visited:
                board[r][c] = "X"
                return True
            
            # When an element an O can change to an X 
            if board[r][c] == "O":
                visited.add((r,c))
                if dfs(r + 1, c) and dfs(r - 1, c) and dfs(r, c + 1) and dfs(r, c - 1):
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        