class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.dict1 = {"2" : "abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.res = []
        
        def dp(i,str1):
            if i == len(digits):
                self.res.append(str1)        
                return 
            
            for c in self.dict1[digits[i]]:
                dp(i+1,str1 + c)
        
        dp(0,"")
        
        return self.res
                
        