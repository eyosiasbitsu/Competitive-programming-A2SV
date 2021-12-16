class Solution:
    def isValid(self, s: str) -> bool:
        symbols = ['(', ')', '{', '}', '[' , ']']
        arr = []
        for i in range(len(s)):
            if len(arr)==0:
                arr.append(s[i])
            elif (s[i] == ')' and arr[-1] == '(') or (s[i] == ']' and arr[-1] == '[') or (s[i] == '}' and arr[-1] == '{'):
                arr.pop()
            else:
                arr.append(s[i])
        if len(arr) == 0:
            return True
        else:
            return False
            
                  