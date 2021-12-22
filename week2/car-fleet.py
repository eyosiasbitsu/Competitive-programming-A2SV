class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        Stuple = zip(position,speed)
        dict1 = dict(Stuple)
        dict2 = {}
        srd = sorted(dict1.items(), key= lambda x:x[0])
        if len(srd) == 1:
            return 1
        result = []
        for i in range(len(srd)-1,-1,-1):
            result.append((target-srd[i][0])/srd[i][1])
            if len(result) > 1 and result[-1] <= result[-2]:
                result.pop()
        return len(result)
