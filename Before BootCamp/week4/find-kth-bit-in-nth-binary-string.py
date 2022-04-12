class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        x = self.findKthBit1(n)
        return x[k-1]
    def findKthBit1(self, n: int) -> str:
        def reverse(s:str)->str:
            return s[::-1]
        def invert(s:str)->str:
            l = list(s)
            for i in range(len(l)):
                if l[i] == "1":
                    l[i] = "0"
                else:
                    l[i] = "1"
            return "".join(l)
        if n == 1:
            return "0"
        x = self.findKthBit1(n-1)
        return x + "1" + reverse(invert(x))