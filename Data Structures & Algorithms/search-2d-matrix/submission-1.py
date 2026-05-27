class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, len(matrix) - 1

        mid = 0

        while top <= bot:
            mid = top + ((bot - top) // 2)
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1 
            else:
                return false
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            midcol = l + ((r - l) // 2)
            if target == matrix[mid][midcol]:
                return true
            elif target < matrix[mid][midcol]:
                r = mid - 1
            elif target > matrix[mid][midcol]:
                l = mid + 1
            else: 
                return false
