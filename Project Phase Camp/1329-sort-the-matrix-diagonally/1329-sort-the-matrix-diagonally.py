class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        dict1 = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dict1[i - j].append(mat[i][j])
        
        for k in dict1:
            dict1[k].sort(reverse = True)
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = dict1[i - j].pop()
        
        return mat
        