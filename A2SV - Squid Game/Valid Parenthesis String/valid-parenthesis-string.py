class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        
        star = 0
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not stack:
                    if star <= 0:
                        return False
                    else:
                        star -= 1    
                else:
                    stack.pop()
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    star += 2
                else:
                    star += 1
                
        return not stack
