class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp_s_t = {}
        mp_t_s = {}
        
        for i in range(len(s)):
            if t[i] in mp_t_s:
                if s[i] != mp_t_s[t[i]]:
                    return False
                continue
            
            if s[i] in mp_s_t:
                if t[i] != mp_s_t[s[i]]:
                    return False
                continue
                
            mp_t_s[t[i]] = s[i]
            mp_s_t[s[i]] = t[i]
        
        return True