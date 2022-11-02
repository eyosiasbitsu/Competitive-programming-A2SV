class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(int)
        for node1, node2 in edges:
            graph[node1] += 1
            graph[node2] += 1
            
            if graph[node1] > 1:
                return node1
            
            if graph[node2] > 1:
                return node2