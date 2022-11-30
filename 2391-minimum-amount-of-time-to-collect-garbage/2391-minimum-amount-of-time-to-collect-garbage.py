class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        _set = set()
        count = 0
        
        for i in range(len(garbage) - 1, -1, -1):
            _set |= set(garbage[i])
            count += len(garbage[i])
            
            garbage[i] = len(_set)
        
        result = 0
        for i in range(len(travel)):
            result += ((travel[i])*garbage[i + 1])
        
        return result + count