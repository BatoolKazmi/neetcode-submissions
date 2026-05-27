class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while m > 0:
            nums1[(m + n) - 1] = nums1[m - 1]
            m -= 1
        print("nums1:", nums1)

        for i in nums2:
            nums1[i - 1] = nums2[i - 1]
        
        return nums1


