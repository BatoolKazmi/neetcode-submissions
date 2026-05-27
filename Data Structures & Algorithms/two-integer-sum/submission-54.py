class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in hash:
                return [hash[res], i]
            hash[n] = i