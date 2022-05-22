class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        
        temp = 0
        while num > 0:
            temp += (num%10)
            num //= 10
        
        return self.addDigits(temp)