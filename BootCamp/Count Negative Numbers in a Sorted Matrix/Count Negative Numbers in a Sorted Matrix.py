class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            while grid[i]:
                x = heapq.heappop(grid[i])
                if x < 0:
                    count+=1
        return count