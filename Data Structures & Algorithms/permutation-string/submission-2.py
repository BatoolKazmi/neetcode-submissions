class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        countS1 = [0]* 26
        countS2 = [0]* 26

        # Check the first few characters length s1
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        
        # Check match & get current match after checking first few characters
        match = 0
        for i in range(26):
            matches += (1 if countS1[i] == countS1[i] else 0)

        # sliding window with l and r
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26: return True
            
            index = ord(s2[r]) - ord('a')
            countS2[index] += 1
            if countS2[index] == countS1[index]:
                match += 1
            elif countS1[index] + 1 == countS2[index]:
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            countS2[index] += 1
            if countS2[index] == countS1[index]:
                match += 1
            elif countS1[index] - 1 == countS2[index]:
                match -= 1
            l += 1
        return match == 26


