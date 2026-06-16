class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        res = 0

        while r < len(arr):
            avg = sum(arr[l:r + 1]) / k 
            if avg >= threshold:
                res += 1
            r += 1
            l += 1

        return res
