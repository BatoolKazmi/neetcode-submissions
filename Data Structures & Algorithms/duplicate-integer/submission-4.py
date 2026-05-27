class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = [1,2,3,3]
        
        for x in nums:
            for k in nums:
                if nums[x] == nums[k]:
                    return true

        return false
