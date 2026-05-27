class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, n in count.items():
            freq[i] = n
        
        res = {}
        for n in range(len(freq) - 1, 0, -1):
            for x in freq(n):
                if len(res) == k:
                    return res
                res.append(x)

        
