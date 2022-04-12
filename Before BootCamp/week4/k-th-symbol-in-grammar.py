class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        prev = self.kthGrammar(n-1,k//2 + k%2)
        if prev == 1:
            if k%2 == 0:
                return 0
            else:
                return 1
        if prev == 0:
            if k%2 == 0:
                return 1
            else:
                return 0
                