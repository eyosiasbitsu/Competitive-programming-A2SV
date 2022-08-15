class Solution:
    def checkRecord(self, s: str) -> bool:
        ca = 0
        cl = 0
        
        for c in s:
            if c == 'A':
                ca += 1
            
            if c != 'L':
                cl = 0
            
            if c == 'L':
                cl += 1
                
            if cl == 3 or ca == 2:
                return False
        
        return True