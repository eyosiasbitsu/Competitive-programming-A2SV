class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for i in range(len(points)):
            points[i] = [sqrt(points[i][0]**2 + points[i][1]**2),points[i][0],points[i][1]]
        points.sort()    
        print(points)
        for i in range(len(points)):
            points[i].pop(0)
        return points[:k]
