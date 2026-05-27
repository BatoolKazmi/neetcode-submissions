class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in enumerate(nums):
            for j in enumerate(nums):
                if nums[i] == nums[j]:
                    return True
        return False
