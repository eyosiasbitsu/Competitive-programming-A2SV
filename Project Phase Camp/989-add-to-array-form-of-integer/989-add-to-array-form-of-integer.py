class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        def numToAr(num):
            ar = []
            
            while num:
                ar.append(num%10)
                num //= 10
                
            return reversed(ar)
        
        def arToNum(ar):
            n = 0
            
            for d in ar:
                n = 10*n + d
                
            return n
        
        num = arToNum(num) + k
        
        return numToAr(num)