class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        array = []

        for i, n in enumerate(nums):
            res[nums[i]] = 1 + res.get(nums[i], 0)
        
        for i, n in enumerate(res):
            if res[n] >= k:
                array.append(n)

        return array
