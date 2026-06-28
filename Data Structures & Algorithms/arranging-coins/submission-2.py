class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        temp = n

        while temp - row > 0:
            row += 1
            temp -= row

        return row