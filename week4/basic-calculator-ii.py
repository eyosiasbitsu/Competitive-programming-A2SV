class Solution:
    def calculate(self, s: str) -> int:
        
            nums = []
            lasOp = None
            cur = 0
            for ch in s:
                if ch == " ":
                    continue
                if ch.isdigit():
                    cur = cur*10 + int(ch)
                  
                    continue
                if not lasOp or lasOp == '+':
                
                    nums.append(cur)
                elif lasOp == '-':
                   
                    nums.append(-cur)
                elif lasOp == '*':
                   
                    nums.append(nums.pop()*cur)
                elif lasOp == '/':
                    
                    nums.append(int(nums.pop()/cur))
                cur = 0
                lasOp = ch 
            if not lasOp or lasOp == '+':
                nums.append(cur)
            elif lasOp == '-':
                nums.append(-cur)
            elif lasOp == '*':
                nums.append(nums.pop() * cur)
            elif lasOp == '/':
                nums.append(int(nums.pop() / cur))
            return sum(nums)
            