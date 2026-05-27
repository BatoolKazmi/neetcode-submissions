class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max = 0
        hash = {}
        
        for i in enumerate(nums):
            hash[nums[i]] += 1
            if hash[nums[i]] > hash[max]:
                max = nums[i]

        return max  

