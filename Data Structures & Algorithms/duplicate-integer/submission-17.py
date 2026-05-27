class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i, num_i in enumerate(nums):  
            for j, num_j in enumerate(nums[i+1:], start=i+1): 
                if num_i == num_j:
                    return True
        return False
