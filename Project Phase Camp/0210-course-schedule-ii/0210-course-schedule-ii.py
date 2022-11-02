class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        color = [0 for _ in range(numCourses)]
        res = []
        graph = defaultdict(list)
        
        for ai, bi in prerequisites:
            graph[bi].append(ai)
        
        def dfs(n):
            if color[n] == 1:
                return False
            
            if color[n] == 2:
                return True
            
            if not graph[n]:
                color[n] = 2
                res.append(n)
                return True
            
            color[n] = 1
            cur = True
            
            for ch in graph[n]:
                cur = cur and dfs(ch)
            
            color[n] = 2
            res.append(n)
            return cur
        
        for i in range(numCourses):
            temp = dfs(i)
            if not temp:
                return []
        
        return res[::-1]
                
                
                
                
                
                
                