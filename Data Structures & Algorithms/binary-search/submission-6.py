class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0

        binarysearch(start, end)

        return -1

    def binarysearch(end, start):
        middle = (end + start) // 2

        if target == nums[middle]:
            return middle
        
        if target > nums[middle]:
            binarysearch(middle, end)

        if target < nums[middle]:
            binarysearch(start, middle)