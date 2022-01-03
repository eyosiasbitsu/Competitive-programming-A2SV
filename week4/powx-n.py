class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n)
        if n == 0:
            return 1
        if n == 1:
            return x
        y = self.myPow(x,n//2)
        if n % 2 == 0:
            return y*y
        if n % 2 != 0:
            return x*y*y