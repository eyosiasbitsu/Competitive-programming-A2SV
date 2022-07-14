class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r,c = len(matrix),len(matrix[0])
        
        mat = [[] for _ in range(c)]
        
        for i in range(r):
            for j in range(c):
                mat[j].append(matrix[i][j])
        
        return mat
    