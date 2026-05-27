class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in nums:
            complement = target - n
            if complement in hashmap:
                return [hashmap[complement], i] 
            hashmap[n] = i
