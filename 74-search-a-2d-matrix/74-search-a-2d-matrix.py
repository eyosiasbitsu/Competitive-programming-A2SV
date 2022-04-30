class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        l = 0
        r = len(matrix) - 1
        def inrange(n,m,o):
            if n <= o and o<= m:
                return True
            else:
                return False
        while l <= r:
            mid1 = (l + r)//2
            # print([l,mid1])
            if inrange(matrix[mid1][0],matrix[mid1][len(matrix[mid1])-1],target):
                templ = 0
                tempr = len(matrix[mid1])-1
                while templ <= tempr:
                    mid2 = templ + (tempr - templ)//2
                    if matrix[mid1][mid2] < target:
                        templ = mid2 + 1
                    elif matrix[mid1][mid2] > target:
                        tempr = mid2 - 1
                    elif matrix[mid1][mid2] == target:
                        return True
                    elif l == r and matrix[mid1][mid2] != target:
                        return False
                # print([templ,mid1])
                return False
            elif matrix[mid1][0] > target:
                r = mid1 - 1
            elif matrix[mid1][0] < target:
                l = mid1 + 1
            elif l == r and not inrange(matrix[mid1][0],matrix[mid1][len(matrix[mid1])-1],target):
                return False
        return False
        
            
        