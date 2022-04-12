class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            t1 = -1*heapq.heappop(stones)
            t2 = -1*heapq.heappop(stones)
#             x <= y --> t2 <= t1
            if t1 != t2:
                t1 = (t1-t2)
                heapq.heappush(stones,-1*t1)
        return -1*stones[-1] if stones else 0