class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        result = []
        
        for char in nums:
            d1[char] = d1.get(char,0) - 1
            
        l2 = list(d1.items())
        
        for i in range(len(l2)):
            l2[i] = l2[i][::-1]
            
        heapq.heapify(l2)
        
        for i in range(k):
            result.append(heapq.heappop(l2)[1])
            
        return result