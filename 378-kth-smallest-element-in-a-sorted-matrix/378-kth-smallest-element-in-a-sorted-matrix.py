class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heapq.heapify(matrix)
        temp = []
        heapq.heapify(temp)
        for i in range(k):
            x = heapq.heappop(matrix)
            # print(x)
            if not x:
                x = heapq.heappop(matrix)
            heapq.heappush(temp,heapq.heappop(x))
            heapq.heappush(matrix,x)
        print(temp)
        return temp[-1]