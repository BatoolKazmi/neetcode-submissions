class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in hashset:
                return [hashset[res], i]
            
            hashset[n] == i 
        
        return "noting"