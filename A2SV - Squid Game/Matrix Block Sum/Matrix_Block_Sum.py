class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        for i in range(len(mat)):
            mat[i].insert(0,0)
        
        add_row = [0]*len(mat[0])
        mat.insert(0, add_row)
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] = mat[i][j] + mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]
        result = [[0 for _ in range(len(mat[0]) - 1)] for _ in range(len(mat) - 1)]

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                block_a = (max(i - k - 1, 0), max(j - k - 1, 0))
                block_b = (max(i - k - 1, 0), min(j + k, len(mat[0]) - 1))
                
                block_c = (min(i + k, len(mat) - 1), min(j + k, len(mat[0]) - 1))
                block_d = (min(i + k, len(mat) - 1), max(j - k - 1, 0))

                result[i - 1][j - 1] = self.blockSum(mat, block_c, block_d, block_b, block_a)

        return result

    def blockSum(self, matrix, block1, block2, block3, block4):
        _sum = (matrix[block1[0]][block1[1]] - 
                    matrix[block2[0]][block2[1]] - 
                        matrix[block3[0]][block3[1]] + 
                            matrix[block4[0]][block4[1]])
        
        return _sum
                
