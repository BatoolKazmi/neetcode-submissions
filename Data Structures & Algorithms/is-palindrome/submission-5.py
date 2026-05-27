class Solution:
    def isPalindrome(self, s: str) -> bool:
        f,b = 0, len(s) - 1
        while f < b:
            if f < b and not self.decode(s[f]):
                f += 1
            if f < b and not self.decode(s[b]):
                b -= 1
            if s[f].lower() != s[b].lower():
                return False
            f = 1 + f
            b = b - 1
        return True
            


    def decode(self, c):
        return (ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9"))
