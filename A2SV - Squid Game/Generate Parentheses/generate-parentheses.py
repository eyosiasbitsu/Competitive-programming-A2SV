class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []        
        self.generate('(', n-1, n, ans)

        return ans
    
    def generate(self, s, openLeft, closeLeft, ans):
            if openLeft==0 and closeLeft==0:
                ans.append(s)
                return 

            if openLeft>0:
                self.generate(s+'(', openLeft-1, closeLeft, ans)
            
            if openLeft<closeLeft and closeLeft>0:
                self.generate(s + ')', openLeft, closeLeft-1, ans)

