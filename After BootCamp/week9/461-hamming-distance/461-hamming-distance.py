class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        dist = 0
        
        while x and y:
            if x&1 != y&1:
                dist += 1
            
            x >>= 1
            y >>= 1
        
        print(x,y)
        while x:
            if x&1:
                dist += 1
            x >>= 1
        
        while y:
            if y&1:
                dist += 1
            y >>= 1
        return dist