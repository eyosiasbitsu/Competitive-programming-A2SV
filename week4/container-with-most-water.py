class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        maxA = j*(min(height[j] , height[i]))
        while (j-i > 1):
            if height[j] < height[i]:
                j-=1
            elif height[i] <= height[i]:
                i += 1 
            if (j-i)*(min(height[j] , height[i])) > maxA:
                maxA = (j-i)*(min(height[j] , height[i]))        
        return maxA