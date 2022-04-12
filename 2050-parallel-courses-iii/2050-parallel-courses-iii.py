
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dict1 = defaultdict(set)
        num = [0]*(n+1)
        
        for i,j in relations:
            dict1[i].add(j)
            num[j] += 1
            
        que = deque()
        
        for i in range(1,len(num)):
            if num[i] == 0:
                que.append(i)
                
        self.max = 0
        self.memo = {}
        
        def dfs(i):
            if i not in dict1:
                self.max = max(time[i-1],self.max)
                return time[i-1]
            
            if i in self.memo:
                return self.memo[i]
            
            if i not in self.memo:
                temp = 0
                
                for j in dict1[i]:
                    temp = max(temp,dfs(j))
                    
                self.memo[i] = temp + time[i-1]
                
            self.max = max(self.max,self.memo[i])
            return self.memo[i]
        
        for i in que:
            dfs(i)
            
        return self.max
            