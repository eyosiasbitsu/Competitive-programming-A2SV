
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numparent = [0]*numCourses
        next1 = defaultdict(set)
        
        for course,pre in prerequisites:
            numparent[course] += 1
            next1[pre].add(course)
        
        que = deque()
        for i in range(numCourses):
            if numparent[i] == 0:
                que.append(i)
        
        count = 0
        
        while que:
            for i in range(len(que)):
                temp = que.popleft()
                for course in next1[temp]:
                    numparent[course] -= 1
                    if numparent[course] == 0:
                        que.append(course)
                count += 1
                
        return count == numCourses
            
        