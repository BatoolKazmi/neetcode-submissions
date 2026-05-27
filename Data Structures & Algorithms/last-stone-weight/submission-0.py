class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stones)

        while len(stone) > 1:
            first = heapq.heappop(stone)
            second = heapq.heappop(stone)
            if second > first:
                heapq.heappush(stone, first - second)
        
        heapq.append(0)
        return heapq[0]   