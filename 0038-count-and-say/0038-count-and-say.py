class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rec(num):
            if num == 1:
                return "1"
            
            st = rec(num - 1)
            nxt = ""
            
            count = 1
            cur = st[0]
            
            for i in range(1, len(st)):
                c = st[i]
                
                if c != cur:
                    nxt += str(count)
                    nxt += cur
                    count = 1
                    cur = c
                    
                else:
                    count += 1
            
            nxt += str(count)
            nxt += cur
            
            return nxt
        
        return rec(n)