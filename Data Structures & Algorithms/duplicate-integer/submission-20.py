class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        hashmap = set()

        for x in nums:
            if x in hashmap:
                return True
            hashmap.add(x)

        return False
        
