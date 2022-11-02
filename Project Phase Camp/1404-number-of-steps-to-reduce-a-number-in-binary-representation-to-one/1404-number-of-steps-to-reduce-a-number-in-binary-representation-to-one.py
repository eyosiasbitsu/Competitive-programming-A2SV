class Solution:
    def numSteps(self, s: str) -> int:
        def adder(arr):
            i = len(arr) - 1
            
            while i >= 0 and arr[i] == "1":
                arr[i] = '0'
                i -= 1
            
            if i == -1:
                arr.appendleft('1')
            
            else:
                arr[i] = '1'
            
        arr = deque(list(s))
        count = 0
        
        while len(arr) > 1:
            if arr[-1] == "1":
                adder(arr)
                count += 1
                
            arr.pop()
            count += 1
            
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            