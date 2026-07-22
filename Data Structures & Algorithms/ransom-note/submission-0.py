class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = Counter(ransomNote)
        have = Counter(magazine)

        for i in need:
            if need[i] > have[i]:
                return False
            if i not in have:
                return False
        return True