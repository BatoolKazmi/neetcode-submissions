class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevNum = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in pevNum:
                return [diff, i]
            prevNum[i] = n
        
        return "noting"