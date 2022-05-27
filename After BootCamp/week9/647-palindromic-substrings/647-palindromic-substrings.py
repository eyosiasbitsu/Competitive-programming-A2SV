class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def length_pali(to_left,to_right):
            num = 0
            
            while ( 0 <= to_left and
                   len(s) > to_right and
                   s[to_left] == s[to_right]):
                to_left -= 1
                to_right += 1
                num += 1
            
            return num
        
        res = 0
        
        for i in range(len(s)):
            res += length_pali(i,i)
            res += length_pali(i,i+1)
        
        return res