class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph)
        
        for i in range(len(graph)):
            if color[i] == 0 and not self.validColor(graph,color,1,i):return False
        return True
    def validColor(self,graph,color,curr,node):
        if color[node] != 0:
            return color[node] == curr
        
        color[node] = curr
        
        for n in graph[node]:
            if not self.validColor(graph,color,-curr,n): return False
        return True
        
        