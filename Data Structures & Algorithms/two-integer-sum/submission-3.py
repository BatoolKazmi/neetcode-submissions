class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNum = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in prevNum:
                return [prevNum[res], i]

            prevNum[n] = i
        
        return null
