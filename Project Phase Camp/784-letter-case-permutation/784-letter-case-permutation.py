class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
#         the function will take curr index and string sofar
        def rec(st,idx):
            if idx == len(s):
                res.append(st)
                return
            
            if s[idx].isalpha():
                if s[idx].isupper():
                    rec(st + s[idx], idx + 1)
                    rec(st + s[idx].lower(), idx + 1)
                
                else:
                    rec(st + s[idx], idx + 1)
                    rec(st + s[idx].upper(), idx + 1) 
            else:
                rec(st + s[idx], idx + 1)
        
        rec("",0)
        
        return res
                