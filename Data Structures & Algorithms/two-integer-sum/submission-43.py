class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for n, i in range(len(nums)):
            res = target - n
            if res in hash:
                return [hash(res), i]