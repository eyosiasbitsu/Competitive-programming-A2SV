class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        
        for i in range(1, n + 1):
            adj[i] = []
        
        for sourse, dest, time in times:
            adj[sourse].append((dest, time))
        
        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        result = 0
        for k in shortest:
            result = max(shortest[k], result)
        
        if not result or len(shortest) < n:
            return -1
        
        return result
        
        