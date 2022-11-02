class Solution:
    def binaryGap(self, n: int) -> int:
        
        arr = []
        dist = 0
        
        while n:
            if n & 1:
                arr.append(dist)
            
            n >>= 1
            dist += 1
        
        result = 0
        for i in range(1,len(arr)):
            result = max(result, arr[i] - arr[i - 1])
        
        return result