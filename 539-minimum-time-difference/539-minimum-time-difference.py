class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def stringToNum(st):
            h = int(st[:2])
            m = int(st[3:])
            return h*60 + m
        
        for i in range(len(timePoints)):
            timePoints[i] = stringToNum(timePoints[i])
        
        timePoints.sort()
        timePoints.append(1440 + timePoints[0])
        
        result = min(timePoints[i] - timePoints[i - 1] for i in range(1, len(timePoints)))
        
        return result