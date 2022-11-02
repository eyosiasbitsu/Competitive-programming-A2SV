class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        r = k
        l = 0
        sm = sum(arr[:k])
        res = 0
        
        if sm // k >= threshold:
            res += 1
            
        while r < len(arr):
            sm += arr[r]
            sm -= arr[l]
            
            if sm // k >= threshold:
                res += 1
                
            l += 1
            r += 1
        
        return res