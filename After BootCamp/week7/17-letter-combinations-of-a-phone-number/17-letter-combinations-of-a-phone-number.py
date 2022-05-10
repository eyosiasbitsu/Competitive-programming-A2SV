class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if the digits string is empty then return empty list since there will
        # not be any string combinations
        
        if not digits:
            return []
        # inorder to know the combination of letters we must first set
        # the relationship between the numbers and the letters, to do this
        # what better datastructure is there other than a dictionary
        
        self.dict1 = {"2" : "abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.res = [] # this is the array we are supposed to return (we'll populate it later)
        
        #
        def dfs(i,str1):
            if i == len(digits):
                self.res.append(str1)        
                return 
            
            for c in self.dict1[digits[i]]:
                dfs(i+1,str1 + c)
        
        dfs(0,"")
        
        return self.res
                
        