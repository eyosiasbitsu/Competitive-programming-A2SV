class Solution:
    def isValid(self, s: str) -> bool:
    
        dict1 = { "]" : "[", "}" : "{", ")" : "("}
        stk = []

        for c in s:
            if stk and c in dict1 and stk[-1] == dict1[c]:
                stk.pop()

            else:
                stk.append(c)

        if not stk:
            return True

        else:
            return False

    
    
    