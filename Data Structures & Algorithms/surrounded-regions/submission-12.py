class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = []
        copy = board

        def dfs(r, c):
            # out of range
            if r == ROWS or c == COLS:
                return False

            # when an element is X remain X
            if board[r][c] == "X" or (r,c) in visited:
                copy[r][c] = "X"
                return True
            
            # When an element an O can change to an X 
            if board[r][c] == "O":
                visited.append((r,c))
                if dfs(r + 1, c) and dfs(r - 1, c) and dfs(r, c + 1) and dfs(r, c - 1):
                    copy[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        
        return copy
        