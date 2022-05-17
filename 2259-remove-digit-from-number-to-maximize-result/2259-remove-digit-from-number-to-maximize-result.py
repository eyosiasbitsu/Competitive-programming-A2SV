class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx = -1
        
        for i in range(len(number)):
            if number[i] == digit:
                if (i + 1 < len(number) and
                    number[i+1] > digit):
                    idx = i
                    break
                    
                idx = i
        
        print(idx)
        return  number[0:idx] + number[idx + 1:] 