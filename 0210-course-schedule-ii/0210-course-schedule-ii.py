class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        path = set()
        res = []
        
        graph = defaultdict(list)
        
        for ai, bi in prerequisites:
            graph[bi].append(ai)
        
        def dfs(n):
            if n in path:
                return False
            
            if n in visited:
                return True
            
            if not graph[n]:
                visited.add(n)
                res.append(n)
                return True
            
            path.add(n)
            cur = True
            for ch in graph[n]:
                cur = cur and dfs(ch)
            
            path.remove(n)
            visited.add(n)
            res.append(n)
            return cur
        
        for i in range(numCourses):
            temp = dfs(i)        
            if not temp:
                return []
        
        return res[::-1]
                
                
                
                
            
            
            
            