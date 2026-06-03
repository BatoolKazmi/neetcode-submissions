class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        print(arr)
        res = 0

        for i in arr[len(arr) - 1]:
            res += 1
        
        return res

