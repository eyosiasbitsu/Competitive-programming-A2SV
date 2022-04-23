class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        indegree = [0 for _ in range(n)]
        children = [[] for _ in range(n)]
        
        for from_, to in edges:
            indegree[to] += 1
            children[from_].append(to)
        
        stk = [node for node in range(n) if indegree[node] == 0]
        ans = [set() for _ in range(n)]
        
        while stk:
            par = stk.pop()
            
            for child in children[par]:
                ans[child].add(par)
                ans[child].update(ans[par])
                indegree[child] -= 1
                
                if indegree[child] == 0:
                    stk.append(child)
                    
        for i in range(len(ans)):
            ans[i] = list(ans[i])
            ans[i].sort()
            
        return ans