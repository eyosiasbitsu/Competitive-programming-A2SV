class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []
        
        for n in arr:
            heapq.heappush(heap, (abs(n - x), n))
        
        res = []
        
        while heap and k > 0:
            p = heapq.heappop(heap)
            res.append(p[1])
            k -= 1
        
        res.sort()
        return res