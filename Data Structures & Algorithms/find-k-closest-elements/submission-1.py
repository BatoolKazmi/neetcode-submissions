class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
       l, r = 0, len(arr) - 1
       res = []
       
      
       
       while l < len(arr) and r > 0 and k != r - l + 1:
        print("l: ", l, "r: ", r, "k: ", k)
    
        if abs(arr[l] - x) < abs(arr[r] - x):
            r -= 1
        elif abs(arr[l] - x) > abs(arr[r] - x):
            l += 1
        elif abs(arr[l] - x) == abs(arr[r] - x) and l < r:
            r -= 1
        
       for n in range(k):
        res.append(arr[l])
        l += 1 
        
       return res