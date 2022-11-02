class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        st = {}
        l = 0
        res = 0
        maxf = 0
        
        for i in range(len(s)):
            st[s[i]] = 1 + st.get(s[i], 0)
            maxf = max(maxf, st[s[i]])
            
            while (i - l + 1) - maxf > k:
                st[s[l]] -= 1
                
                if st[s[l]] == 0:
                    del st[s[l]]
                
                l += 1
                
            res = max(i - l + 1, res)
            
        return res
            
            
            
            
            
            
            