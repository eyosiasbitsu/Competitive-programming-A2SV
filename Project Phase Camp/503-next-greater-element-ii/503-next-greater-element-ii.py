class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res = [-1 for _ in range(len(nums))]
        stk = []
        
        i = len(nums) - 1
        
        while i >= 0:
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            
            if stk:
                res[i] = nums[stk[-1]]
            
            stk.append(i)
            i -= 1
            
        i = len(nums) - 1
        
        while i >= 0:
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            
            if stk and res[i] == -1:
                res[i] = nums[stk[-1]]
            
            stk.append(i)
            i -= 1
        
        return res
        
        
        
        
        
        
        
        
        
        
        