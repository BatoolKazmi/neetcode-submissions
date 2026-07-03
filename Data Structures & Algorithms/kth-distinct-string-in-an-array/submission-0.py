class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = 0
        hashmap = {}

        for i in range(len(arr)):
            hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1
        
        for n in hashmap:
            if hashmap[n] == 1:
                distinct += 1
            if distinct == k:
                return n 


        if distinct < k:
            return ""