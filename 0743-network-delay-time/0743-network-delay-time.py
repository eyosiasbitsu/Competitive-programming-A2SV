class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {}
        result = {}
        min_heap = []
        
        for i in range(1, n + 1):
            adj[i] = []
        
        for src, dst, weight in times:
            adj[src].append((dst, weight))
        
        heapq.heappush(min_heap, (0, k))
        
        while min_heap:
            cur_weight, cur_node = heapq.heappop(min_heap)
            
            if cur_node in result:
                continue
            
            result[cur_node] = cur_weight
            for neigh, weight in adj[cur_node]:
                if neigh not in result:
                    heapq.heappush(min_heap, (cur_weight + weight, neigh))
        
        if len(result) < n:
            return -1
        
        min_time = 0
        for node in result:
            min_time = max(min_time, result[node])
        
        return min_time
            
            
            
            
            
            
            
            