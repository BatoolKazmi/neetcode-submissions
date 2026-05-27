class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0

        self.binarysearch(nums, target, start, end)

        return -1

    def binarysearch(nums, target, end, start):
        middle = (end + start) // 2

        if target == nums[middle]:
            return middle
        
        if target > nums[middle]:
            binarysearch(nums, target, middle + 1, end)

        if target < nums[middle]:
            binarysearch(nums, target, start, middle - 1)