class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        
        for i in range(len(arr)):
            arr[i] = list(arr[i])
            
        for ar in arr:
            l = 0
            r = len(ar) - 1
            while l < r:
                if ar[l] and ar[r]:
                    ar[l], ar[r] = ar[r], ar[l]
                    l += 1
                    r -= 1

                elif not ar[l]:
                    l += 1

                elif not ar[r]:
                    r -= 1
        
        for i in range(len(arr)):
            arr[i] = "".join(arr[i])
            
        return " ".join(arr)
    
    
    
    
    
    
    
    
    