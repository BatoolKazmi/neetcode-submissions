class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        maxLen = max(len(word1), len(word2))
        x, y = 0, 0
        word3 = ""

        for i in range(maxLen):

            if x < len(word1)  and y < len(word2):
                word3 += word1[x]
                word3 += word2[y] 
            elif y < len(word2):
                word3 += word2[y]
            elif x < len(word1):
                word3 += word1[x]
            
            x += 1
            y += 1

        return word3
