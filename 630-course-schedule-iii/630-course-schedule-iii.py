class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        time = 0
        courses.sort(key = lambda x:x[1])
        heap = []
        
        for el in courses:
            print(el[0],el[1])
            if time + el[0] <= el[1]:
                heapq.heappush(heap,-1*el[0])
                time += el[0]
                
            else:
                if heap:
                    if el[0] < -1*heap[0]:
                        time -= (-1*heapq.heappop(heap))
                        time += el[0]
                        heapq.heappush(heap,-1*el[0])
                    
        return len(heap)
    
    
# 		for ele in courses:
# 			if ele[0]+time<=ele[1]:
# 				heappush(h,-ele[0])
# 				time+=ele[0]

# 			else:
# 				if h:
# 					if ele[0]<-h[0]:
# 						time-=-(heappop(h))
# 						time+=ele[0]
# 						heappush(h,-ele[0])
        