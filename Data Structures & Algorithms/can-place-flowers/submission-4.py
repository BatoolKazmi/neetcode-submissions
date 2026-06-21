class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            if i == 0 and i + 1 < len(flowerbed):
                count += 1 if flowerbed[i] == 0 and flowerbed[i + 1] == 0 else 0
                flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                count += 1 if flowerbed[i] == 0 and flowerbed[i - 1] == 0 else 0 
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1
        
        return True if count >= n else False