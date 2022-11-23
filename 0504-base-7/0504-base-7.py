class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return "0"
        
        st = ""
        md = []
        
        if num < 0:
            st = "-"
            
        num = abs(num)
        while num != 0:
            md.append(num%7)
            num //= 7
        
        for i in range(len(md) - 1, -1, -1):
            st += str(md[i])
        
        return st