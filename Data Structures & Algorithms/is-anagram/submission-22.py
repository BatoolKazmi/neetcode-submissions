class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for c in s:
            countS[ord(c) - ord("a")] = 1 + countS.get(ord(c) - ord("a"), 0)
            countT[ord(c) - ord("a")] = 1 + countT.get(ord(c) - ord("a"), 0)
        
        return countS == countT

        
    

        