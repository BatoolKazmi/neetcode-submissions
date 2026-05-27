class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # One of the values
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]: 
                continue;
            # initializing the 2 pointers
            l, r = i + 1, len(nums) - 1
            # two Sums with 2 pointer
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]]);
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
