class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        group_idx = {}
        result = []
        
        for i in range(len(groupSizes)):
            groupSizes[i] = (groupSizes[i], i)
        
        groupSizes.sort()
        i = 0
        
        for size, idx in groupSizes:
            if size not in group_idx:
                result.append([])
                group_idx[size] = i
                i += 1
                
            result[group_idx[size]].append(idx)
            if len(result[group_idx[size]]) == size:
                del group_idx[size]
        
        return result
            
            
            
            
            
            
            