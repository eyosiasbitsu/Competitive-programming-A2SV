class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxHeap = []
        heapify(maxHeap)
        
        for i in target:
            heappush(maxHeap, -1*i)
            
        s = sum(target)
        while maxHeap[0] != -1:
            largest = -1*heappop(maxHeap)
            restSum = s - largest
            if s >= 2*largest or s == largest:
                return False
            previousValue = largest % restSum
            if previousValue == 0:
                previousValue = restSum
            heappush(maxHeap, -1*previousValue)
            s -= largest
            s += previousValue
        return True