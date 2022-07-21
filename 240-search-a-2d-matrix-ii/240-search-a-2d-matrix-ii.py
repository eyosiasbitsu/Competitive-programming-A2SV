class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            row = matrix[i]

            if row[-1] < target:
                continue
            
            if row[0] > target:
                break
            
            l,r = 0,len(row) - 1

            while l <= r:
                mid = (l + r)//2

                if row[mid] < target:
                    l = mid + 1
                
                elif row[mid] > target:
                    r = mid - 1
                
                else:
                    return True
        
        return False