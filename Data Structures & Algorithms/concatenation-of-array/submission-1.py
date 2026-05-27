class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        double = 2 * len(nums)
        ans = [0] * double

        for i, n in enumerate(nums):
            ans[i] = nums[i]
            ans[i + length] = nums[i]
        
        return ans

