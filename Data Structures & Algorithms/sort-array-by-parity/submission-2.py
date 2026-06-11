class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        pos = 0

        while pos < len(nums):
            if nums[pos] % 2 == 0:
                res[l] = nums[pos]
                l += 1
            else: 
                res[r] = nums[pos]
                r -= 1
            pos += 1
        return res