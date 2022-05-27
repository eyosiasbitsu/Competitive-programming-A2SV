class Solution:
    def checkString(self, s: str) -> bool:
        flag = False
        
        for c in s:
            if flag and c == 'a':
                return False
            if c == 'b':
                flag = True
        
        return True