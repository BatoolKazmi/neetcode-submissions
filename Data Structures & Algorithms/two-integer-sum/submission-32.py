class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = {}

        for i, n in nums:
            res = target - n
            if res in hashset:
                return True
            hashset.add(n)
        
        return hashset
