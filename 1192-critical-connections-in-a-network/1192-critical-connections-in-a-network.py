class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dis = [0]*n
        low = [0]*n
        self.time = 0
        
        visited = set()
        output = []
        graph = defaultdict(list)
        
        for s,t in connections:
            graph[s].append(t)
            graph[t].append(s)
        
        def dfs(cur,prev):
            visited.add(cur)
            self.time += 1
            dis[cur] = low[cur] = self.time
            
            for nxt in graph[cur]:
                if nxt not in visited:
                    dfs(nxt,cur)
                    low[cur] = min(low[cur],low[nxt])
                    
                elif nxt != prev:
                    low[cur] = min(low[cur],dis[nxt])
                
                if low[nxt] > dis[cur]:
                    output.append([cur,nxt])
        
        dfs(0,-1)
        
        return output
        
         