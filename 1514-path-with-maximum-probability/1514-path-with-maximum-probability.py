class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for i in range(len(edges)):
            edge = edges[i]
            prob = succProb[i]
            
            adj[edge[0]].append((edge[1], succProb[i]))
            adj[edge[1]].append((edge[0], succProb[i]))
            
        seen = set()
        maxHeap = [(-1, start, start)]
        seen.add(start)
        
        while maxHeap:
            cur_prob, cur_node, par = heapq.heappop(maxHeap)
            if cur_node == end:
                print(cur_prob)
                return -1*cur_prob
            
            for next_node, next_prob in adj[cur_node]:
                if next_node != par:
                    seen.add(next_node)
                    heapq.heappush(maxHeap, (cur_prob*next_prob, next_node, cur_node))
        
        return 0
        
        
        
        
        
        
        
        