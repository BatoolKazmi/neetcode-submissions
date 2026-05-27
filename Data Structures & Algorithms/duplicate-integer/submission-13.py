class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in enumerate(nums):
            for j in enumerate(i + 1, nums):
                if nums[i] == nums[j]:
                    return True
        return False
