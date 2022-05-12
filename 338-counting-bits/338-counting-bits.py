class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ar = []
        
        for i in range(num+1):
            ar.append(self.count(i))
        
        return ar
        
    def count(self,n):
        return bin(n).count("1")