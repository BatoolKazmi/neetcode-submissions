class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for n, i in enumerate(nums):
            res = target - n
            print(res)
            if res in hash:
                return [hash(res), i]
            hash[n] = i