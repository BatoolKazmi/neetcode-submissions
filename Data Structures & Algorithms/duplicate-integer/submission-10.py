class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for x in nums:
            for k in nums:
                if x == k:
                    return True
                    k += k
            
            x += x

        return False
