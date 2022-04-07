class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -1 * heapq.heappop(stones)
            s2 = -1 * heapq.heappop(stones)
            if s1 == s2:
                continue
            else:
                s1 = s1 - s2
                heapq.heappush(stones,-1*s1)
        return 0 if not stones else -1*stones[0]