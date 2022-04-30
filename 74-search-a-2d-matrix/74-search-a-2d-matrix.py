class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.bs(0,len(matrix[mid])-1,matrix[mid],target)
            
            elif matrix[mid][0] < target:
                l = mid + 1
                
            elif matrix[mid][0] > target:
                r = mid - 1
        
    def bs(self,l,r,arr,target):
        
        while l <= r:
            mid = (l+r)//2

            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                return True
            
        return False
                    