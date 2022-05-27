class Solution:
    def thousandSeparator(self, n: int) -> str:
        ar = []
        t = n
        
        while n:
            ar.append(n%10)
            n //= 10
        
        res = ""
        l = 0
        
        if len(ar) <= 1:
            return str(t)
        
        for n in ar:
            res = str(n) + res
            l += 1
            
            if l == 3:
                res = "." + res
                l = 0
        print(res)
        return res[1:] if res[0] == '.' else res
        