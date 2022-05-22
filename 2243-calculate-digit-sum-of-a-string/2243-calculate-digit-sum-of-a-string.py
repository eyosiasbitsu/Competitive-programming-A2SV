class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        
        res = ""
        i = 0
        
        while i < len(s):
            t = k
            temp = 0
            
            while i < len(s) and t > 0:
                temp += int(s[i])
                i += 1
                t -= 1
                
            res += str(temp)
        
        return self.digitSum(res,k)
    