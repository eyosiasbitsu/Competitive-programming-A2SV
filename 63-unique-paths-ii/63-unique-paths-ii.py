class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if (obstacleGrid[0][0] ==1 or 
            obstacleGrid[-1][-1] == 1):
            return 0
        
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dirs = [(0,1),(1,0)]
        
        cach = {}
        cach[(m-1,n-1)] = 1
        
        def dfs(i,j):
            if (obstacleGrid[i][j] == 1):
                return 0
            
            if (i,j) not in cach:
                temp = 0
                
                for i_add,j_add in dirs:
                    new_i,new_j = i + i_add, j_add + j
                    
                    if (0<= new_i < m and 
                        0 <= new_j < n):
                        temp += dfs(new_i,new_j)
                        
                cach[(i,j)] = temp
            
            return cach[(i,j)]
            
        return dfs(0,0)