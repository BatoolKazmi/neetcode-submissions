class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()

        for i, n in enumerate(nums):
            res = target - n
            if res in hashset:
                return [hashset[n], i]
            hashset.add(n)
        
        return "noting"