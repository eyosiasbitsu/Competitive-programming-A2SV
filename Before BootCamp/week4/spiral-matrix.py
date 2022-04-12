class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cl = 0
        cr = len(matrix[0]) - 1
        cd = len(matrix) - 1
        cu = 0
        result = []
        while cu <= cd and cl <= cr:
            for i in range(cl,cr+1):
                result.append(matrix[cu][i])
            cu+=1
            if cu > cd or cl > cr:
                break
            for i in range(cu,cd+1):
                result.append(matrix[i][cr])
            cr-=1
            if cu > cd or cl > cr:
                break
            for i in range(cr,cl-1,-1):
                result.append(matrix[cd][i])
            cd-=1
            if cu > cd or cl > cr:
                break
            for i in range(cd,cu-1,-1):
                result.append(matrix[i][cl])
            cl+=1
            if cu > cd or cl > cr:
                break
        return result
                