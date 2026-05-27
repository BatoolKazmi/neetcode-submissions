class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 1
        
        for n in nums:
            print(j)
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
            elif abs(i - j) <= k:
                j += 1
            elif abs(i - j) > k:
                i += 1
        
        return False