class Solution:
    def maxDifference(self, s: str) -> int:
        map = {}
        maxOdd = 0
        minEven = float('inf')

        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
                
            print(map)
        
        for n in map:
            print(map[n] % 2)
            if map[n] % 2 != 0:
                maxOdd = max(maxOdd, map[n])
            else:
                minEven = min(minEven, map[n])
            print("maxOdd: ", maxOdd)
            print("minEven: ", minEven)

        return maxOdd - minEven
