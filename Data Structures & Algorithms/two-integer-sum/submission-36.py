class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in hashset:
                return [nums[res], nums[n]]
            hashset[n].append(i)