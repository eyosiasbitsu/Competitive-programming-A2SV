class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        r,c = len(matrix),len(matrix[0])
        cach = {}
        
        def dfs(i,j):
            
            if (i,j) not in cach:
                cach[(i,j)] = 1
                temp = 0
                
                for i_add,j_add in dirs:
                    new_i,new_j = i_add + i, j_add + j
                    if (0<= new_i < r and
                       0 <= new_j < c and
                       matrix[new_i][new_j] > matrix[i][j]):
                        temp = max(temp,dfs(new_i,new_j))
                        
                cach[(i,j)] += temp
                
            return cach[(i,j)]
        
        res = 0
        
        for row in range(r):
            for col in range(c):
                dfs(row,col)
                res = max(cach[(row,col)],res)
            
        return res