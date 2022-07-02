class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        verticalCuts.append(w)
        horizontalCuts.append(h)
        
        verticalCuts.sort()
        horizontalCuts.sort()
        
        l = verticalCuts[0]
        i = 1
        
        while i < len(verticalCuts):
            l = max(verticalCuts[i] - verticalCuts[i - 1],l)
            i += 1
            print()
        
        w = horizontalCuts[0]
        i = 1
        
        while i < len(horizontalCuts):
            w = max(horizontalCuts[i] - horizontalCuts[i - 1],w)
            i += 1
        print(l,w)
        return (l*w)%(10**9 + 7)
            
            
            
            