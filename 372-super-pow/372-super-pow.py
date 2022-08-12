class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = 0
        
        if a == 1:
            return 1
        
        for i in range(len(b)):
            num = 10*num + b[i]
            
        print(num)
        
        def p(a,n):
            
            if n == 0:
                return 1
            
            if n == 1:
                return a
            
            temp = p(a, n//2) % 1337
            
            return temp*temp*(p(a,n%2) % 1337)
        
        return p(a, num)%1337
            