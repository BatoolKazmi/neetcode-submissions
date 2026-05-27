class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = []

        for n in nums:
            hashmap = num[n]
            if target - n in num:
                return [hashmap[n], num[n]] 

        return 