class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        f = 0

        while s < len(nums) and f < len(nums):
            if nums[f] != 0 and s != f:
                nums[s] = nums[f]
                nums[f] = 0
            if nums[s] != 0:
                s += 1
            f += 1
            print(nums)
        