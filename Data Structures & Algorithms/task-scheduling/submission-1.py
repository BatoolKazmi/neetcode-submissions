class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                temp = 1 + heapq.heappop(maxHeap)
                q.push([temp, time + n])
            
            if q and q[0][1] == time:
                heapq.heappop(maxHeap, q.pop(value))
        
        return time
                
