class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        r = []
        ans = 0
        i = 0
        j = len(height)-1
        while i < len(height) and j >= 0:
            if not l:
                l.append(height[i])
            else:
                l.append(max(height[i],l[-1]))
            if not r:
                r.append(height[j])
            else:
                r.append(max(height[j],r[-1]))
            i += 1
            j -= 1
        r = r[::-1]
        for i in range(len(height)):
            x = min(r[i],l[i])
            if x - height[i] > 0:
                ans+=(x - height[i])
        return ans 
            
        
        