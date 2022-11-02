class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        res = min(height[l], height[r])*(r - l)
        
        while r != l:
            if height[r] <= height[l]:
                r -= 1
            
            else:
                l += 1
            
            res = max(res, min(height[l], height[r])*(r - l))
        
        return res