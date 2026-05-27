class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 if len(nums) >= 1 else 0
        n, i = len(nums), 0
        nex = i + 1
        while (i < n and nex < n):
            if nums[i] < nums[nex]:
                nums[i + 1] = nums[nex]
                i += 1
                k += 1
            elif nums[i] == nums[nex] and nex < len(nums):
                nex += 1
        return k