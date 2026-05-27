class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in nums:
            complement = target - n
            hashmap = {complement}
            if complement in hashmap:
                return [num[n], i] 
