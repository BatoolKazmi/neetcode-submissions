class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxRes = 0
        hashmap = {}

        for i in range(len(arr)):
            hashmap[arr[i]] = 1 + hashmap.get(arr[i], 0)

        for num, count in hashmap.items():
            if num == count:
                maxRes = max(maxRes, num)
        return maxRes if maxRes != 0 else - 1