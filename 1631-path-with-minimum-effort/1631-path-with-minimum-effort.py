class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def dfs(k,i,j):
            visited.add((i,j))
            for i_add,j_add in dirs:
                new_i,new_j = i+i_add,j+j_add
                
                if (0<= new_i<m and 
                    0<=new_j<n and 
                    (new_i,new_j) not in visited):
                    new_k = abs(heights[i][j]-heights[new_i][new_j])
                    if new_k<=k:
                        dfs(k,new_i,new_j)
        l,r = -1,max([heights[a][b] for a in range(m) for b in range(n)])
        
        while l+1<r:
            
            mid = (l+r)//2
            visited = set()
            dfs(mid,0,0)
            if (m-1,n-1) in visited:
                
                r = mid
            else:
                l = mid
        return r
                    
                    
                