class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expectedNums = [] 
        k = 0

        for i, n in enumerate(nums):
            if nums[i] != val:
                k += 1
                expectedNums.append(nums[i])
        
        for i, n in enumerate(nums):
            if i >= len(expectedNums):
                nums[i] = None
            else:
                nums[i] = expectedNums[i]
        
        return k
            