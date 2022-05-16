class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         times[i] = (from,to, takes)
        graph = defaultdict(list)
    
        for fr,to,takes in times:
            graph[fr].append((to,takes))
        
        visited = set()
        minheap = [(0,k)]
        t = 0
        
        while minheap:
            w1,nxt = heapq.heappop(minheap)
            
            if nxt in visited:
                continue
            
            visited.add(nxt)
            t = max(w1,t)
            
            for ch,w in graph[nxt]:
                if ch not in visited:
                    heapq.heappush(minheap,(w1 + w,ch))
        
        return t if len(visited) == n else -1