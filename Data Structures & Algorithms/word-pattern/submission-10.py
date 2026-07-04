class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = {}
        letters = {}
        
        split = s.split()

        if len(split) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in words and split[i] not in letters:
                words[pattern[i]] = split[i]
                letters[split[i]] = pattern[i]
            elif (pattern[i] in words and words[pattern[i]] != split[i]) or (split[i] in letters and letters[split[i]] != pattern[i]):
                return False

        return True

            