class Solution:
    def countPoints(self, rings: str) -> int:
        dict1 = defaultdict(set)
        res = 0
        
        for i in range(0,len(rings)-1,2):
            if rings[i] not in dict1[rings[i + 1]]:
                dict1[rings[i + 1]].add(rings[i])
                
                if len(dict1[rings[i + 1]]) == 3:
                    res += 1
        
        return res