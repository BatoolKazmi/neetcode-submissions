class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        double = 2 * len(nums)
        ans = [0] * double

        for i, n in enumerate(nums):
            print("this is the index:", i)
            ans[i] = nums[i]
            ans[i + length] = nums[i]
            # [0, 1, 2, 3] [4, 5, 6, 7]
            print(i, "+", length, "=", (i + n))
        
        return ans

