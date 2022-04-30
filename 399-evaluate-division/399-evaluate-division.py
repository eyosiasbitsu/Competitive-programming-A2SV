class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph =defaultdict(dict)
        
        for i in range(len(equations)):
            n1 = equations[i][0]
            n2 = equations[i][1]
            val = values[i]
            
            graph[n1][n2] = val
            graph[n2][n1] = 1/val
        
        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1
            
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,y,visited)
                    if temp == -1:
                        continue
                        
                    return temp*graph[x][i]
            
            return -1
        
        out = []
        
        for p,q in queries:
            out.append(dfs(p,q,set()))
        
        return out
                