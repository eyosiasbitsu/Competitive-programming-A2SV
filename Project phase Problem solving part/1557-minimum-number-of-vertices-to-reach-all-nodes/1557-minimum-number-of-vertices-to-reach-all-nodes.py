class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        mark = [0 for i in range(n)]
        
        for fr, to in edges:
            mark[to] += 1
        
        res = [i for i in range(len(mark)) if mark[i] == 0]
        
        return res