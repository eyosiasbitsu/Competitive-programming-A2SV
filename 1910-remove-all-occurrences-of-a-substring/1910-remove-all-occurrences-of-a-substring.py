class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        # n - 4 k - 2
        N, K = len(s), len(part)
        if K > N:
            return s
        stack = []
        for i, char in enumerate(s):
            stack.append(char)
            if len(stack) >= K and "".join(stack[-K:]) == part:
                stack = stack[0:-K]

        return "".join(stack)