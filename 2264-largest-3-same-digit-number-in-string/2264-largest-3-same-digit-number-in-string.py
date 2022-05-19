class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = ""
        res = ""
        temp = 0
        
        for i in range(len(num)):
            if not n or n[-1] == num[i]:
                n += num[i]
            
            elif n[-1] != num[i]:
                n = num[i]
            
            if len(n) == 3:
                if int(n[0]) >= temp:
                    res = n
                    n = n[0]
                    temp = int(n)
        
        return res
                