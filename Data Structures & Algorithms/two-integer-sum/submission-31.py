class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()

        for n in nums:
            res = target - n
            if res in hashset:
                return True
            hashset.add(n)
        
        return hashset
