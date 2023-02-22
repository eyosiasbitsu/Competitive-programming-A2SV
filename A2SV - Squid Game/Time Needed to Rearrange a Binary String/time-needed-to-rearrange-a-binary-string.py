class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        nearestOneTime = 0
        j = 0
        
        for i in range(len(s)):
            if s[i] == "1":
                if i != j:
                    nearestOneTime = max(nearestOneTime+1,i-j)
                
                j += 1
        
        return nearestOneTime
