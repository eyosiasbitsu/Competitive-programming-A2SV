class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = []
        
        while n:
            binary.append(n & 1)
            n >>= 1
        
        while len(binary) < 32:
            binary.append(0)
            
        res = 0
        p = 0
        
        for i in range(len(binary) - 1, -1, -1):
            
            res += (binary[i] * 2**p)
            p += 1
            
        return res
        
        