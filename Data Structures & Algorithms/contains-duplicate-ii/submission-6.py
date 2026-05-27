class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 1
        
        while j < len(nums) - 1:
            if k == 0:
                return False
            print(j)
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
            elif abs(i - j) <= k:
                j += 1
            elif abs(i - j) > k:
                i += 1
        
        return False