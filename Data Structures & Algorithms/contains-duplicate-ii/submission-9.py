class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, len(nums) - 1
        
        while j < len(nums):
            if k == 0:
                return False
            print(j)
            if nums[i] == nums[j] and abs(i - j) <= k and i != j:
                print("i: ", i, "j: ", j)
                print("nums[i]: ", nums[i], "nums[j]: ", nums[j])
                return True
            elif abs(i - j) <= k:
                j -= 1
            elif abs(i - j) > k:
                i += 1
        
        return False