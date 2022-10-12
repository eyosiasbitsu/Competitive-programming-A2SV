class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        arr = [0, 0, 0]
        
        l = 0
        r = 0
        res = 0
        
        while r < len(s):
            while r < len(s) and not (arr[0] and arr[1] and arr[2]):
                idx = ord(s[r]) - ord("a")
                if idx < 3:
                    arr[idx] += 1
                
                r += 1
                
            # "acbbcac"
               # 0123456
                
            while (arr[0] and arr[1] and arr[2]):
                res += (len(s) - r + 1)
                idx = ord(s[l]) - ord("a")
                if idx < 3:
                    arr[idx] -= 1
                
                l += 1
                
        return res
    
    
    
    
    