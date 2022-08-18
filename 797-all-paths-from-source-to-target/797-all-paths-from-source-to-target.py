class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        ar = []
        
        def dfs(i):
            if i == len(graph) - 1:
                temp = ar[:]
                temp.append(i)
                res.append(temp)
                return
            
            ar.append(i)
            for neigh in graph[i]:
                dfs(neigh)
                
            ar.pop()
            
        dfs(0)
        return res