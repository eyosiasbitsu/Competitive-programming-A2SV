class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            if n in seen:
                return False
            
            temp = str(n)
            nxt = 0
            seen.add(n)
            
            for c in temp:
                nxt += (int(c)**2)
            
            n = nxt
            
            if n == 1:
                return True