class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1])
        
        capacity = 0
        
        for box,per in boxTypes:
            if truckSize >= box:
                capacity += box*per
                truckSize -= box
            
            else:
                capacity += truckSize*per
                break
        
        return capacity