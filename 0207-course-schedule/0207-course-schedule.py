class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         
            adj = [[] for _ in range(numCourses)]
            indegree = [0 for _ in range(numCourses)]
            topSort = []
            
            for src, dest in prerequisites:
                adj[src].append(dest)
                indegree[dest] += 1
            
            queue = deque([])
            for i in range(numCourses):
                if indegree[i] == 0:
                    queue.append(i)
            
            while queue:
                cur = queue.popleft()
                topSort.append(cur)
                
                for child in adj[cur]:
                    indegree[child] -= 1
                    
                    if indegree[child] == 0:
                        queue.append(child)
            
            return len(topSort) == numCourses
                    
                    
                    
                    
                    
                    
                    
            
            
            
            
            
            
            