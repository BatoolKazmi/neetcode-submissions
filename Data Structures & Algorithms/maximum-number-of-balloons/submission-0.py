class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        new = {}

        for i in range(len(text)):
            new[text[i]] = 1 + new.get(text[i], 0)
        
        res = float('inf')
        for c, need in hashmap.items():
            if c not in new:
                return 0
            possible = new[c] // need
            res = min(res, possible)
            
        return res