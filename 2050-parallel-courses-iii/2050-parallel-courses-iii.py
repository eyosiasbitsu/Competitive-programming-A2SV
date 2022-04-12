
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        self.dict1 = defaultdict(set)
        self.num = [0]*(n+1)
        
        for i,j in relations:
            self.dict1[j].add(i)
            self.num[i] += 1
            
        que = deque()
        print(self.dict1)
        for i in range(1,len(self.num)):
            if self.num[i] == 0:
                que.append(i)
                
        self.max = 0
        self.memo = {}
        
        def dfs(i):
            if i not in self.dict1:
                self.max = max(time[i-1],self.max)
                return time[i-1]
            
            if i in self.memo:
                return self.memo[i]
            
            if i not in self.memo:
                temp = 0
                
                for j in self.dict1[i]:
                    temp = max(temp,dfs(j))
                    
                self.memo[i] = temp + time[i-1]
                
            self.max = max(self.max,self.memo[i])
            return self.memo[i]
        
        for i in que:
            dfs(i)
            
        return self.max
            