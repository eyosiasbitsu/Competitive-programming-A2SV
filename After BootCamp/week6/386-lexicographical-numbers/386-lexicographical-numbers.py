class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ar = []
        
        for i in range(1,n+1):
            ar.append(str(i))
        
        ar.sort()
        
        for i in range(len(ar)):
            ar[i] = int(ar[i])
        
        return ar