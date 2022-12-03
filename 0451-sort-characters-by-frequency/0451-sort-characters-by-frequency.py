class Solution:
    def frequencySort(self, s: str) -> str:
        
        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1
        
        heap = []
        for char in frequency:
            heapq.heappush(heap, (-frequency[char], char))
        
        result = []
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char*(-freq))
        
        return "".join(result)
        