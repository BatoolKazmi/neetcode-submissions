class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSort(l, r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[r] = pivot, nums[p]

            if p > k: return quickSort(l, r - 1)
            elif p < k: return quickSort(l + 1, r)
            elif p == k: return nums[p]
        
        return quickSort(0, len(nums) - 1)
