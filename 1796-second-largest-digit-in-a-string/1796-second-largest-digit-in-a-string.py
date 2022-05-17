class Solution:
    def secondHighest(self, s: str) -> int:
        ar = []
        
        for c in s:
            if c.isdigit():
                heapq.heappush(ar,-int(c))
        
        if not ar:
            return -1
        
        m = heapq.heappop(ar)
        
        while ar and ar[0] == m:
            heapq.heappop(ar)
        
        return -ar[0] if ar else -1