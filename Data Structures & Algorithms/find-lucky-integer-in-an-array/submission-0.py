class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxRes = 0
        hashmap = {}

        for i in range(len(arr)):
            hashmap[arr[i]] = 1 + hashmap.get(arr[i], 0)

        for i in range(len(arr)):
            if hashmap[arr[i]] == arr[i]:
                maxRes = max(maxRes, arr[i])
        
        return maxRes if maxRes != 0 else - 1