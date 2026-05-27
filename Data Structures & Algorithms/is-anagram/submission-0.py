class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashset = set()

        for char in s:
            char.hashset.add()
        
        for char in t:
            if char != hashset:
                return False
        
        return True


        