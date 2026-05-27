class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0

        for i, n in range(len(nums)): 
            print(n)
            if n-1 not in res:
                length = 1
                while (n + length) in res:
                    length += 1
                    print(length)
                    print(longest)
                    longest = max(length, longest)
        return longest
        