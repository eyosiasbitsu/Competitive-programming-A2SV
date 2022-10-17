class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        stk = []
        res = 0
        
        for i in range(len(nums)):
            n = nums[i]
            if n != 0 and stk:
                temp = stk[-1] - stk[0] + 1
                res += int((temp)*((temp + 1)/2))
                stk = []
                
            while stk and n == 0 and i - stk[-1] != 1:
                stk.pop()
            
            if n == 0:
                stk.append(i)
          
        if stk and stk[-1] == len(nums) - 1:
            temp = stk[-1] - stk[0] + 1
            res += int((temp)*((temp + 1)/2))
            
        return res
    
    
    
    
    
    
    
    
    
    