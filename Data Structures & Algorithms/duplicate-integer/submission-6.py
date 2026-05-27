class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = [1,2,3,4]
        
        for x in nums:
            for k in nums:
                if nums[x] == nums[k]:
                    return True

        return False
