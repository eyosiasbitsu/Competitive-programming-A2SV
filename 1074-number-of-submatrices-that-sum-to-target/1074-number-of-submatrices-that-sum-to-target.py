class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
            matrix[i] = [0] + matrix[i]
            
        ans = 0
        d = defaultdict(int)
        
        for col1 in range(n):
            for col2 in range(col1+1, n+1):
                temp, d[0] = 0, 1
                
                for r in range(m):
                    temp += matrix[r][col2] - matrix[r][col1]
                    if(temp - target in d):
                        ans += d[temp - target]
                        
                    d[temp] += 1
                    
                d.clear()
                
        return ans