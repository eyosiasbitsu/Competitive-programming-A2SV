class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        for i in range(len(arr)):
            arr[i] = (abs(arr[i] - x), arr[i])
        
        heapq.heapify(arr)
        
        res = []
        
        while k > 0:
            res.append(heapq.heappop(arr))
            k -= 1
            
        for i in range(len(res)):
            res[i] = res[i][1]
        
        res.sort()
        
        return res