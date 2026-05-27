class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, n in ennumerate(nums):
            if n == target:
                return i

        return -1