class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        
        new = [[0 for _ in range(c)] for _ in range(r)]
        
        k = 0
        for i in range(m):
            for j in range(n):
                new[k//c][k%c] = mat[i][j]
                k += 1
        
        return new
        