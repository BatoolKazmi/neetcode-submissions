class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = -1

        for i in range(len(nums)):
            if prev != -1 and ( (prev % 2 == 0 and nums[i] % 2 == 0) or (prev % 2 != 0 and nums[i] % 2 != 0) ):
                return False
            prev = nums[i]
        
        return True