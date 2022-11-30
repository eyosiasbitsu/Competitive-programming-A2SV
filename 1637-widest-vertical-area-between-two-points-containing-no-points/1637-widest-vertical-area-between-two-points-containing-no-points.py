class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        for i in range(len(points)):
            points[i] = points[i][0]
        
        points.sort()
        res = -1
        
        for i in range(1, len(points)):
            res = max(res, points[i] - points[i - 1])
        
        return res