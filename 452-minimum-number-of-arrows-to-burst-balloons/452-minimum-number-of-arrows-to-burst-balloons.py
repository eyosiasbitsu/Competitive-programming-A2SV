class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x:x[1])
        
        pt = points[0][1]
        count = 1
        
        for i in range(1,len(points)):
            
            temp = points[i][0]
            temp2 = points[i][1]
            
            if temp > pt:
                pt = temp2
                count += 1
                
        return count
        