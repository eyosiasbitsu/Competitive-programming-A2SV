class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.dict1 = {}
        
        def dp(l, i):
            if l == len(triangle) - 1:
                return triangle[l][i]
            
            if (l,i) not in self.dict1:
                self.dict1[(l,i)]  = triangle[l][i] + min(dp(l + 1, i),
                                            dp(l + 1, i + 1))
                
            return self.dict1[(l,i)]
        
        return dp(0,0)
            
            