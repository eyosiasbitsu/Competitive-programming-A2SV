class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        HEAP = []
        heapq.heapify(HEAP)
        i = 0
        while i < len(heights) - 1:
            if heights[i + 1] <=  heights[i]:
                i += 1
                continue
            dif  = heights[i + 1] - heights[i]
            if dif <= bricks:
                heapq.heappush(HEAP,-1*dif)
                bricks -= dif
            else:
                if ladders > 0:
                    if HEAP and abs(HEAP[0]) > dif:
                        bricks += (-1*heapq.heappop(HEAP))
                        ladders -= 1
                        heapq.heappush(HEAP,-1*dif)
                        bricks -= dif
                    else:
                        ladders -= 1
                else:
                    break
            i += 1
        return i