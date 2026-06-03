class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0

        for i in range(len(t)):
            if l > len(s) - 1:
                return True
            if s[l] == t[i]:
                l += 1
            
        
        if l > len(s) - 1:
            return True
        else:
            return False

