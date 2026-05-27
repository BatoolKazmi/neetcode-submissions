class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        row = 0

        while top <= bot:
            mid = top + ((bot - top) // 2)
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1 
            else:
                row = mid
                break
        else:
            return False
        
        l, r = 0, COLS - 1

        while l <= r:
            midcol = l + ((r - l) // 2)
            if target == matrix[row][midcol]:
                return True
            elif target < matrix[row][midcol]:
                r = mid - 1
            elif target > matrix[row][midcol]:
                l = mid + 1
            
        return False
