class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        lost = {}
        for winner, loser in matches:
            if winner not in lost:
                lost[winner] = 0
            
            lost[loser] = 1 + lost.get(loser, 0)
        
        result = [[],[]]
        for k in lost:
            if lost[k] == 0:
                result[0].append(k)
            
            elif lost[k] == 1:
                result[1].append(k)
                
        result[0].sort()
        result[1].sort()
        
        return result