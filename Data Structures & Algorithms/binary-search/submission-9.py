class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0

        return self.binarysearch(nums, target, start, end)

    def binarysearch(self, nums: List[int], target: int, start: int, end: int):
        if start > end:
            return -1

        middle = (end + start) // 2

        if target == nums[middle]:
            return middle
        
        if target > nums[middle]:
            return self.binarysearch(nums, target, middle + 1, end)

        if target < nums[middle]:
            return self.binarysearch(nums, target, start, middle - 1)
    