class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = set()
        l, r = 0, 0
        total = sum(nums)

        print("total: ",total)

        if total < target:
            return 0
        
        while l < len(nums) and r < len(nums):
            res.add(nums[r])

            if target > sum(res): 
                r += 1
            elif target < sum(res):
                res.remove(nums[l])
                l += 1
                
        return len(res)
            




            