class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini = 0
        l, r = 0, 0
        res = float('inf')
        
        while l < len(nums) and r < len(nums):
        
            if r - l == k - 1:
                mini = nums[r] - nums[l]
                res = min(res, mini)
                l += 1
            r += 1

        return res 