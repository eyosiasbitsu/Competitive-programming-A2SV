class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = 0
        
        for car in s:
            if car == letter:
                c += 1
        
        return (c*100)//len(s)