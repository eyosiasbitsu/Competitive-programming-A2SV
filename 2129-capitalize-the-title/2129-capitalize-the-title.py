class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ar = title.split()
        
        for i in range(len(ar)):
            if len(ar[i]) == 2 or len(ar[i]) == 1:
                ar[i] = ar[i].lower()
             
            else:
                ar[i] = ar[i][0].upper() + ar[i][1:].lower()
        
        res = " ".join(ar)
        
        return res