class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        time = 0
        courses.sort(key = lambda x:x[1])
        heap = []
        
        for el in courses:
            if time + el[0] <= el[1]:
                heapq.heappush(heap,-1*el[0])
                time += el[0]
                
            elif heap and el[0] < -1*heap[0]:
                    time -= (-1*heapq.heappop(heap))
                    time += el[0]
                    heapq.heappush(heap,-1*el[0])
                    
        return len(heap)
