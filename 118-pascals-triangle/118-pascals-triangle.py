class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res  = []
        
        while numRows:
            if not res:
                res.append([1])
            
            else:
                temp = [1]
                
                for i in range(1,len(res[-1])):
                    temp.append(res[-1][i] + res[-1][i - 1])
                
                temp.append(1)
                res.append(temp)
            
            numRows -= 1
        
        return res