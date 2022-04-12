class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ar = list(range(1,n+1))
        a = ar[::-1]
        x = len(a) 
        while x > 1:
            for i in range(k-1):
                a.insert(0,a.pop())
            a.pop() 
            x -= 1
        return a[0]