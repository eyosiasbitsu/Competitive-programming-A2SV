class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def rec(n,k):
            if n == 0:
                return 1
            
            temp = 0
            for i in range(k,5):
                temp += rec(n-1,i)
            
            return temp
        
        return rec(n,0)