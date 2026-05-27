class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        l = 0
        res = 0

        for r in s:
            while s[r] in subset:
                subset.remove()
                s.remove(l)
                l += 1
            right += 1
            res = max(subset, r - l + 1)
        return res