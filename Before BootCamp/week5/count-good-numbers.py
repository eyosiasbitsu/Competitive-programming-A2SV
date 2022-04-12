class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def myPow(x:int , n: int) -> int:
            if n < 0:
                x = 1/x
                n = abs(n)
            if n == 0:
                return 1
            if n == 1:
                return x
            y = myPow(x,n//2)%1000000007
            if n % 2 == 0:
                return y*y
            if n % 2 != 0:
                return x*y*y
        return (myPow(5, n//2 + n%2)*myPow(4, n//2))%(10**9 + 7)