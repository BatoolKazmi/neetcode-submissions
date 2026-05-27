class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashset = set()

        for char in s:
            hashset.add(char)
        
        for char in t:
            if char not in hashset:
                return False
        
        return True


        