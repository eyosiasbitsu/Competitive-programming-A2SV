class Solution:
    def fib(self, n: int) -> int:
        self.dict1 = {}
        def fib(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n not in self.dict1:
                self.dict1[n] = fib(n - 1) + fib(n-2)
                
            return self.dict1[n]
        return fib(n)
            