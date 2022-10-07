class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        cach = {}
        res = []
        
        def dfs(i, arr):
            if i == len(graph) - 1:
                res.append(arr)
                return
            
            if not graph[i]:
                return
            
            for to in graph[i]:
                dfs(to, arr + [to])

            return
        
        dfs(0, [0])
        return res
    
    
    
    
    
    
    
    
    
    
    