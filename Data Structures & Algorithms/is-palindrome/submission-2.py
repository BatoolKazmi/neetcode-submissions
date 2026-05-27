class Solution:
    def isPalindrome(self, s: str) -> bool:
        f,b = 0, len(s) - 1
        while f < b:
            if f < b and not self.decode(s[l]):
                l = 1 + l
            if f < b and not self.decode(s[r]):
                r = r - 1
            if s[l].lower != s[r].lower:
                return False
            l = 1 + l
            r = r - 1
        return True
            


    def decode(self, c):
        return (ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9"))
