class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for x in nums:
            for k in nums:
                if nums[x] == nums[k]:
                    return True

        return False
