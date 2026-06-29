class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
                
            if mid % 2 == 1: # odd
                if nums[mid] != nums[mid - 1]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # even
                if nums[mid] != nums[mid + 1]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return nums[l]
        