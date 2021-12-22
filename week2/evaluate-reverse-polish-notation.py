class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        result = 0
        for char in tokens:
            if char not in op:
                stack.append(char)
            else:
                x = int(stack.pop())
                y = int((stack.pop()))
                if char == '+':
                    z = x + y
                elif char == '-':
                    z = y - x
                elif char == '*':
                    z = x*y
                elif char == '/':
                    z = int(y/x)
                stack.append(z)
        return stack[-1]
                