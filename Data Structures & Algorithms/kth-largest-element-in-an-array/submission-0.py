class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)

        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        
        return res