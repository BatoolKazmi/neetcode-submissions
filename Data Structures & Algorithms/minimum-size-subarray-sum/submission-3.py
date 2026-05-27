class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = set()
        l, r = 0, 0
        total = sum(nums)
        res.add(nums[r])

        print("total: ",total)

        if total < target:
            return 0
        
        while l < len(nums) and r < len(nums):
            if target > sum(res): 
                r += 1
                res.add(nums[r])
            elif target < sum(res):
                res.remove(nums[l])
                l += 1
            else:
                return len(res)

        return len(res)
            




            