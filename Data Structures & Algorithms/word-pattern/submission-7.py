class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        split = s.split()
        if len(split) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashmap and split[i] not in hashmap.values():
                hashmap[pattern[i]] = split[i]
            elif pattern[i] not in hashmap or hashmap[pattern[i]] != split[i]:
                return False

        return True

            