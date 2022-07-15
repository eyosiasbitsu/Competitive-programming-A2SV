class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set1 = set(arr)
        count = 0
        
        for n in arr:
            if n == 0:
                count += 1
                
        if count > 1:
            return True
        
        for n in arr:
            if 2*n in set1 and n != 0:
                return True
        
        return False