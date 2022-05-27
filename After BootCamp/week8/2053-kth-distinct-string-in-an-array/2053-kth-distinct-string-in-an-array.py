class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ar = []
        idx = {}
        idx2 = {}
        
        for i in range(len(arr)):
            c = arr[i]
            
            if c not in idx:
                ar.append(1)
                idx[c] = len(ar) - 1
                idx2[len(ar) - 1] = c
            else:
                ar[idx[c]] += 1
        
        count = 0
        
        for i in range(len(ar)):
            if ar[i] == 1:
                count += 1
            
            if count == k:
                return idx2[i]
        
        return ""