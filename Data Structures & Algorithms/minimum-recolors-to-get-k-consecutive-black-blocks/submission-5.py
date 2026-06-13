class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        res = len(blocks) + 1
        count = 0

        while l < len(blocks) and r < len(blocks):
            print("res: ", res, "blocks[r]: ", blocks[r], "l: ", l, "r: ", r, "count: ", count)
            
            if blocks[r] == "W":
                count += 1
            if r - l > k - 1:
                count -= 1 if blocks[l] == "W" else 0 
                l += 1
            if r - l == k - 1:
                res = min(res, count)
            r += 1

       
        return res

