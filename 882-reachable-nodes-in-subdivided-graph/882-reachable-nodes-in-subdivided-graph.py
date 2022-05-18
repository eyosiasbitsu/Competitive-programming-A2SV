class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        output = 0
        
        for fr,to,weight in edges:
            graph[fr].append((to,weight + 1))
            graph[to].append((fr,weight + 1))
       
        dist = [float("inf")]*n
        dist[0] = 0
        h = [(0,0)]
        
        while h:
            node,sofar = heappop(h)
            
            for nxt, steps in graph[node]:
                total = steps + sofar
                
                if total <= dist[nxt]:
                    dist[nxt] = total
                    heappush(h,(nxt,total))
         
        for s,t,w in edges:
            w1,w2 = maxMoves - dist[s],maxMoves - dist[t]
            output += (max(0,w1) + max(0,w2))
            
            if w1 >= 0 and w2 >= 0:
                output -= max(0,w1 + w2 - w)
        
        for d in dist:
            if d <= maxMoves:
                output += 1
        
        return output